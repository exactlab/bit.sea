import numpy as np

def get_2_indices_for_slicing(array,MinValue,MaxValue, istart):
    n = len(array)
    for i in range(istart, n):
        if array[i]> MinValue:
            MinIndex=i
            break
    for i in range(MinIndex,n):
        if array[i]> MaxValue:
            MaxIndex=i
            break
    return MinIndex, MaxIndex

def array_of_indices_for_slicing(xcoarse, xfine):
    '''
    Returns two arrays, having the same size of xcoarse
    I_START, I_END
    
    '''
    
    jpi = len(xcoarse)
    deltax = np.diff(xcoarse).mean() # 1./16
    I_START = np.zeros((jpi,),np.int)
    I_END   = np.zeros((jpi,),np.int)
    istart = 0
    for ji in range(jpi):
        centrocella = xcoarse[ji]
        bordoW = centrocella-deltax/2
        bordoE = centrocella+deltax/2
        istart, iend = get_2_indices_for_slicing(xfine, bordoW, bordoE, istart)
        I_START[ji] = istart
        I_END[ji]   = iend
    return I_START, I_END


def interp_2d_by_cells_slices(Mfine, Maskout, I_START, I_END, J_START, J_END, fillValue=-999.0):
    '''
    
    '''
    jpk, jpj, jpi = Maskout.shape
    tmask = Maskout.mask_at_level(0)
    OUT = np.ones((jpj,jpi),np.float32)*fillValue
    
    for ji in range(jpi):
        istart = I_START[ji]
        i_end  =   I_END[ji]
        # istart == iend if Coarse grid is out of Fine grid
        if istart == i_end : continue
        for jj in range(jpj):
            jstart = J_START[jj]
            j_end  =   J_END[jj]
            if tmask[jj,ji]:
                localcell = Mfine[jstart:j_end, istart:i_end]
                goods = localcell>0
                if np.any(goods):
                    OUT[jj,ji] = localcell[goods].mean()
    return OUT


if __name__== "__main__":

    from commons.mask import Mask
    from Sat import SatManager as Sat
    TheMask=Mask('/pico/home/usera07ogs/a07ogs00/OPA/V2C/etc/static-data/MED1672_cut/MASK/meshmask.nc')
    tmask = TheMask.mask_at_level(0)

    jpk,jpj,jpi = TheMask.shape
    x = TheMask.xlevels[0,:]
    y = TheMask.ylevels[:,0]

    x1km = Sat.masks.KD490mesh.lon
    y1km = Sat.masks.KD490mesh.lat

    I_START, I_END = array_of_indices_for_slicing(x, x1km)
    J_START, J_END = array_of_indices_for_slicing(y, y1km)


    inputfile="/gss/gss_work/DRES_OGS_BiGe/Observations/TIME_RAW_DATA/STATIC/SAT/KD490/WEEKLY/ORIGMESH/20010522_d-OC_CNR-L3-KD490-MedOC4AD4_SAM_1KM-MED-REP-v01.nc"
    Kext = Sat.readfromfile(inputfile,'KD490')

    KEXT_16=interp_2d_by_cells_slices(Kext, TheMask, I_START, I_END, J_START, J_END)

    Sat.dump_simple_V4file('test.nc',KEXT_16,'KD490')
        

            
    