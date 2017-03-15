#!/bin/env python

from extern.matrix2latex import matrix2latex

import os.path
import collections
import re
import math

###########################################################
# Regions, Samples and Labels
###########################################################

regions = collections.OrderedDict( [
    ('SR', ('h_bprimemass_SR', None) ),
    ('CR, 1aH, 2sj' , ('h_bprimemass_CRB', None) ),
    ('CR, 1H, 1sj'    , ('h_bprimemass_CRC', None) ),
    ('CR, 1aH, 1sj'     , ('h_bprimemass_CRD', None) ),
    ]
)

data = [
    'Data'
    ]
signal = [
    'BprimeBToHB1000',
    'BprimeBToHB1800'
    ]
backgrounds = [
    'QCD',
    'TT',
#    'WJets',
#    'ZJets',
#    'DYQQ',
#    'WJetsQQ',
    ]

labels = {
    # Region labels
    'SR':r'A',
    'CR, 1aH, 2sj': 'B',
    'CR, 1H, 1sj': 'C',
    'CR, 1aH, 1sj': 'D',
    'BprimeBToHB1000': r'$M_{B}\;\ 1000\;\mathrm{GeV}$',
    'BprimeBToHB1800': r'$M_{B}\;\ 1800\;\mathrm{GeV}$',
    'ZJets': r'Z$\rightarrow\nu\nu$',
    'TT': r't$\bar{\textnormal{t}}$',
    'QCD': r'QCD',
#    'WJets': r'W + Jets',
#    'WJetsQQ': r'W(qq)',
#    'DYQQ': r'DY(qq)',
    }


###########################################################
# Yield helper class
###########################################################


class Yields(object):
    """docstring for Yields"""

    _backgrounds_label = 'Backgrounds'

    def __init__(self,regions, bkgs, labels={}):
        super(Yields, self).__init__()
        self.backgrounds = bkgs
        self.regions = regions
        self.labels = labels
        self.values = { r:{} for r in regions }

    @property
    def samples(self):
        return self.backgrounds

    def backgroundSums(self):

        sums = { r:{} for r in regions }

        for r in self.regions:
            nbkg = 0
            e2bkg = 0

            for s in self.backgrounds:
                nev,err = self.values[r][s]

                nbkg += nev
                e2bkg += err**2

            sums[r][self._backgrounds_label] = (nbkg, e2bkg**0.5)

        return sums

    def ascii(self):
        for r in self.regions:
            print 'Region:',r
            for s in self.samples:
                print '   ',s,'(%.1f+/-%.1f)' % self.values[r][s]

    def latex(self, bkgsum=False):
        matrix = []
        hdr = ['']+[ self.labels[r] if r in self.labels else r for r in self.regions]
        hdr += ['A/C'] +['B/D']
        import copy
        # Copy values, in case we need to mangle them
        values = copy.deepcopy(self.values)

        if bkgsum:
            for r in self.regions:
                sums = self.backgroundSums()
                values[r].update(sums[r])

            samples = self.backgrounds+[self._backgrounds_label]
        else:
            samples = self.backgrounds

        for s in samples:

            # row starts with sample name
            row = [self.labels[s] if s in self.labels else s]

            # followed by events and errors in order
            row += [ '$%.2f \pm %.2f$' % values[r][s] for r in self.regions ]

            ratio1 = 100*(values["SR"][s])[0]/(values["CR, 1H, 1sj"][s])[0]
            ratio2 = 100*(values["CR, 1aH, 2sj"][s])[0]/(values["CR, 1aH, 1sj"][s])[0]
            err1 =  100 * math.sqrt( pow((values["SR"][s])[1]/(values["CR, 1H, 1sj"][s])[0],2)  + pow( ((values["SR"][s])[0]/pow((values["CR, 1H, 1sj"][s])[0],2)) *  (values["CR, 1H, 1sj"][s])[1],2))
            err2 =  100 * math.sqrt( pow((values["CR, 1aH, 2sj"][s])[1]/(values["CR, 1aH, 1sj"][s])[0],2)  + pow( ((values["CR, 1aH, 2sj"][s])[0]/pow((values["CR, 1aH, 1sj"][s])[0],2)) *  (values["CR, 1aH, 1sj"][s])[1],2))
       
            
            
            
            row += [ '$(%.2f  \pm %.2f)$'  % (ratio1, err1)  + '$\%$'  ]
            row += [ '$(%.2f \pm %.2f)$' % (ratio2, err2)  + '$\%$' ]
            matrix.append(row)

        # Create the table
        table =  matrix2latex(matrix,headerRow=hdr)

        rows = table.splitlines()
        # create a regex that matches all rules
        reRules = re.compile(r'(\\toprule|\\midrule|\\bottomrule)')

        # replace lines with rules (hoping doens't break anything)
        rows = [ reRules.sub(r'\hline',r) for r in rows ]


        if bkgsum:
            for i,r in enumerate(rows):
                # search for the table block
                try:
                    j = r.index('&')
                except:
                    # not found
                    continue

                if not self._backgrounds_label in r[:j]: continue

                # count how many tabs to re-insert
                m = re.search('[^\t]', r)
                # m.start is the first non-tab
                # '\t'*m.start() is a string with n tabs
                tabs = '\t'*m.start() if m else ''
                # insert additional horizontal lines : order matters!
                rows.insert(i+1,tabs+'\hline')
                rows.insert(i,tabs+'\hline')
                break

        table = '\n'.join(rows) 
                    
        return table




###########################################################
# Class to fill a Yeild obj based on a region definiton set
###########################################################
class ChannelYieldFiller(object):
    """docstring for ChannelYieldFiller"""
    def __init__(self, regions, histopath, channel):
        super(ChannelYieldFiller, self).__init__()
        self.regions = regions
        self.histopath = histopath
        self.channel = channel

    def fill( self, yields ):
         # Import ROOT only here, to avoid it interfering with parsing
        from ROOT import TFile, TH1, Double

        for s in yields.samples:
            for r in yields.regions:
                filename = s+'_'+self.channel+'.root'
                filepath = os.path.join(self.histopath,filename)
                hname,rng = self.regions[r]

                rf = TFile(filepath)
                if rf.IsZombie():
                    raise RuntimeError('Failed to open %s',filepath)
                htmp = rf.Get(hname)
                # print htmp
                if not isinstance(htmp,TH1):
                    raise RuntimeError('Histogram %s not found in %s' % (hname,filepath))

                h = htmp.Clone()
                # Adapt the range, if required
                xax = h.GetXaxis()
                first, last = xax.GetFirst()+4, xax.GetLast()
                print "----->", first
                
                xmin, xmax = xax.GetBinLowEdge(first), xax.GetBinUpEdge(last)
                print "---->", xmin
                if rng is not None:
                    umin,umax = rng
                    umin = umin if umin is not None else xmin
                    umax = umax if umax is not None else xmax

                    # print umin,umax
                    # Apply new range (use ROOT to do the difficult bit :P)
                    xax.SetRangeUser(umin,umax)
                
                    # Update limits
                    first, last = xax.GetFirst() + 4, xax.GetLast()
                    print "---->" ,first
                    xmin, xmax = xax.GetBinLowEdge(first), xax.GetBinUpEdge(last)
                    print "---->", xmin

                err = Double(0.)
                nev = h.IntegralAndError(first,last,err)
                rf.Close()

                print filename, hname,rng,
                print ' | ','%.2f(%d)'%(xmin,first),'-', last,'%.2f(%d)'%(xmax,last), ' -- ', nev,err

                del h

                yields.values[r][s] = (nev,err)       


###########################################################
# Main body
###########################################################
if __name__ == '__main__':

    import optparse

    usage = 'usage: %prog -l lumi'
    parser = optparse.OptionParser(usage)
    parser.add_option('-c', '--channel', dest='channel', type='string', default = 'semileptonic', help='Channel to analyze: semileptonic or fullhadronic')
    (opt, args) = parser.parse_args()

    basepath = 'output'
    histodir = 'histos_Mo17_20Feb'

    if opt.channel =='cat0_singleH':
        chanLabel = 'singleh'

        # And the yields to fill
        yields = {
            'signalRegions': Yields( ['SR', 'CR, 1aH, 2sj', 'CR, 1H, 1sj', 'CR, 1aH, 1sj'], backgrounds, labels=labels ),
            'controlRegions': Yields( ['SR', 'CR, 1aH, 2sj','CR, 1H, 1sj', 'CR, 1aH, 1sj'], backgrounds, labels=labels ),
        }

    elif opt.channel == 'cat1_singleH':
        chanLabel = 'singleh'

        # And the yields to fill
        yields = {
            'signalRegions': Yields( ['SR', 'CR, 1aH, 2sj', 'CR, 1H, 1sj', 'CR, 1aH, 1sj'], backgrounds, labels=labels ),
            'controlRegions': Yields( ['SR', 'CR, 1H, 1sj', 'CR, 1aH, 2sj', 'CR, 1aH, 1sj'], backgrounds, labels=labels ),
        }

    else:
        parser.error('What channel?')

    # Where are the histograms?
    histopath = os.path.join(basepath,chanLabel,histodir)

    # Create a filler object
    filler = ChannelYieldFiller(regions, histopath, opt.channel)

    # destination directory
    outtables = 'output/%s/tables' % (chanLabel,)
    if not os.path.exists(outtables):
        os.makedirs(outtables)
    
    for name,y in yields.iteritems():
        print 'Calculating yeilds:',name
        filler.fill(y)

        # print some details
        y.ascii()
        
        table = y.latex(bkgsum=True)

        # more debug stuff
        print table


        with open(outtables+'/'+name+'_'+opt.channel+'_bkg.tex','w') as dottex:
            dottex.write(table)

