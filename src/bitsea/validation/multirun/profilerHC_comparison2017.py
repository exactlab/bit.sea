#!/usr/bin/env python
# Author: Giorgio Bolzon <gbolzon@ogs.trieste.it>
# Script to generate profiles of model files in
# the same time and locations where instruments
# such as bioFloats, mooring or vessels have been found.

# When imported, this scripts only defines settings for matchup generation.
from bitsea.instruments.lovbio_float import FloatSelector

from bitsea.instruments.matchup_manager import Matchup_Manager
from bitsea.commons.time_interval import TimeInterval
from bitsea.commons.Timelist import TimeList
from bitsea.basins.region import Rectangle
# location of input big ave files, usually the TMP directory.
# ave files are supposed to have N3n, O2o and chl

RUN_REF ='HC_2017_simdd'
RUN_DA  ='HC_2017_assw'

INPUTDIR ='/gpfs/scratch/userexternal/ateruzzi/' + RUN_REF +'/wrkdir/MODEL/AVE_FREQ_1/'

# output directory, where aveScan.py will be run.

BASEDIR = {}

BASEDIR[RUN_REF] = '/gpfs/scratch/userexternal/ateruzzi/ELAB_HC2017/VALID_float/' + RUN_REF + '/PROFILATORE/'
BASEDIR[RUN_DA] = '/gpfs/scratch/userexternal/ateruzzi/ELAB_HC2017/VALID_float/' + RUN_DA + '/PROFILATORE/'


#DATESTART = '20140101'
DATESTART = '20170101'
DATE__END = '20171231'

T_INT = TimeInterval(DATESTART,DATE__END, '%Y%m%d')
TL = TimeList.fromfilenames(T_INT, INPUTDIR,"ave*.nc",filtervar="N1p")

ALL_PROFILES = FloatSelector(None,T_INT, Rectangle(-6,36,30,46))


# vardescriptorfile="/gpfs/scratch/userexternal/ateruzzi/ELAB_HC2017/VALID_float/bit.sea/validation/multirun/VarDescriptor_HC2017.xml"

#This previous part will be imported in matchups setup.

# The following part, the profiler, is executed once and for all.
# It might take some time, depending on length of simulation or size of files.
# if __name__ == '__main__':
#     # Here instruments time and positions are read as well as model times
#     M = Matchup_Manager(ALL_PROFILES,TL,BASEDIR)


#     profilerscript = BASEDIR + 'jobProfiler.sh'
#     aggregatedir="/pico/scratch/userexternal/gbolzon0/eas_v12/eas_v19_3/wrkdir/POSTPROC/output/AVE_FREQ_1/TMP/"
#     M.writefiles_for_profiling(vardescriptorfile, profilerscript, aggregatedir=aggregatedir) # preparation of data for aveScan

#     M.dumpModelProfiles(profilerscript) # sequential launch of aveScan
