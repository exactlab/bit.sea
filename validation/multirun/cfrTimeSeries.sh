# Comparison of time series of different runs

#RUN_LIST = [CR_COAST, DA_COAST_01]
#VAR_LIST = [P_i, ppn]
# Non so come passarli

export MASKFILE=/pico/home/usera07ogs/a07ogs00/OPA/V4/etc/static-data/MED1672_cut/MASK/meshmask.nc

python extract_satTimeSeries.py

SATDIR=/gss/gss_work/DRES_OGS_BiGe/Observations/TIME_RAW_DATA/STATIC/SAT/CCI/NEW_20161702/WEEKLY_V4/
OUTSAT=/pico/scratch/userexternal/ateruzzi/BITDOTSEA/bit.sea/validation/multirun/
OUTDIR=$CINECA_SCRATCH/ELAB_DA_COAST/OUTPUTvalidation/CFRTIMESER/
INDIR=$CINECA_SCRATCH/
TXTPATH=/wrkdir/POSTPROC/output/AVE_FREQ_1/STAT_PROFILES/

mkdir -p $OUTDIR

python extract_satTimeSeries.py -o $OUTSAT -i $SATDIR -y 2013

python plot_cfrTimeSeries.py -o $OUTDIR -i $INDIR -t $TXTPATH -s $OUTSAT