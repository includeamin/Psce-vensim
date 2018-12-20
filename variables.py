

vars_PCSE = {
    'SMFCF - Field capacity of the soil':
        {'cód': 'SMFCF', 'unids': 'Dmnl', 'ingr': True, 'egr': True, 'arch': 'crop'},
    'SM0 - Porosity of the soil':
        {'cód': 'SM0', 'unids': 'Dmnl', 'ingr': True, 'egr': True, 'arch': 'soil'},
    'SMW - Soil moisture content at wilting point':
        {'cód': 'SMW', 'unids': 'Dmnl', 'ingr': True, 'egr': True, 'arch': 'soil'},
    'CRAIRC - Soil critical air content (waterlogging)':
        {'cód': 'CRAIRC', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'soil'},
    'SOPE - Maximum percolation rate root zone':
        {'cód': 'SOPE', 'unids': 'cm/day', 'ingr': True, 'egr': False, 'arch': 'soil'},
    'KSUB - Maximum percolation rate of water to subsoil':
        {'cód': 'KSUB', 'unids': 'cm/day', 'ingr': True, 'egr': False, 'arch': 'soil'},
    'K0 - Hydraulic conductivity of saturated soil':
        {'cód': 'K0', 'unids': 'cm/day', 'ingr': True, 'egr': False, 'arch': 'soil'},
    'RDMSOL - Maximum rooting depth allowed by soil':
        {'cód': 'RDMSOL', 'unids': 'cm', 'ingr': True, 'egr': True, 'arch': 'soil'},
    'SSMAX - Maximum surface storage':
        {'cód': 'SSMAX', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'site'},
    'SSI - Initial surface storage':
        {'cód': 'SSI', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'site'},
    'LOSST - Total water percolated to deep soil':
        {'cód': 'LOSST', 'unids': 'cm', 'ingr': False, 'egr': True, 'arch': 'result'},
    'TRA - Crop transpiration rate':
        {'cód': 'TRA', 'unids': 'cm/day', 'ingr': False, 'egr': True, 'arch': 'result'},
    'RD - Depth of actual root zone':
        {'cód': 'RD', 'unids': 'cm', 'ingr': False, 'egr': True, 'arch': 'result'},
    'TSUMEM - temperature sum from sowing to emergence':
        {'cód': 'TSUMEM', 'unids': 'cel day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TBASEM - Base temperature for emergence':
        {'cód': 'TBASEM', 'unids': 'cel', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TEFFMX - maximum effective temperature for emergence':
        {'cód': 'TEFFMX', 'unids': 'cel', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TSUM1 - Temperature sum from emergence to anthesis':
        {'cód': 'TSUM1', 'unids': 'C/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TSUM2 - Temperature sum from anthesis to maturity':
        {'cód': 'TSUM2', 'unids': 'C/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'IDSL -  Switch for phenological development options temperature':
        {'cód': 'IDSL', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DLO - Optimal daylength for phenological development':
        {'cód': 'DLO', 'unids': 'hr', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DLC - Critical day length':
        {'cód': 'DLC', 'unids': 'hr', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DVSI - Initial development stage':
        {'cód': 'DVSI', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DVSEND - Final Development stage':
        {'cód': 'DVSEND', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DTSMTB - Daily increase in temperature sum as a function of daily mean temperature':
        {'cód': 'DTSMTB', 'unids': 'C/d', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DVS- Development stage':
        {'cód': 'DVS', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'TSUM - Temperature Sum':
        {'cód': 'TSUM', 'unids': 'C/day', 'ingr': False, 'egr': True, 'arch': 'result'},
    'FRTB -Fraction of total dry matter increase partitioned to roots as a function of development stage':
        {'cód': 'FRTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FSTB -Fraction of above ground dry matter increase partitioned to stems as a function of development '
    'stage':
        {'cód': 'FSTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FLTB - Fraction of above ground dry matter increase partitioned to leaves as a function of development '
    'stage':
        {'cód': 'FLTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FOTB - Fraction of above ground dry matter increase partitioned to storage organs as a function of '
    'development stage':
        {'cód': 'FOTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'VERNSAT - Saturated vernalisation requirements':
        {'cód': 'VERNSAT', 'unids': 'day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'VERNBASE - Base vernalisation requirements':
        {'cód': 'VERNBASE', 'unids': 'day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'VERNRTB - Rate of vernalisation as a function of daily mean temperature':
        {'cód': 'VERNRTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'VERNDVS - Critical development stage after which the effect of vernalisation is halted':
        {'cód': 'VERNDVS', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'AMAXTB - Maximum leaf CO2 assimilation rate as a function of development stage of the crop':
        {'cód': 'AMAXTB', 'unids': 'kg/ha/ha', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'EFFTB - Initial light-use efficiency of CO2 assimilation of single leaves as function of daily temperature':
        {'cód': 'EFFTB', 'unids': '(kg/ha/hr)/(J/m2/sec);C', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'KDIFTB - Extinction coefficient for diffuse visible light as function of development stage':
        {'cód': 'KDIFTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TMPFTB - Reduction factor of AMAX as function of average temperature':
        {'cód': 'TMPFTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TMNFTB - Reduction factor of gross assimilation rate as function of low minimum temperature':
        {'cód': 'TMNFTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'LAI - Leaf area index':
        {'cód': 'LAI', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'Q10 - Relative change in respiration rate per 10 ºC temperature change':
        {'cód': 'Q10', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RMR - Relative maintenance respiration rate roots':
        {'cód': 'RMR', 'unids': 'kg (CH2O)/kg/d', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RMS - Relative maintenance respiration rate stems':
        {'cód': 'RMS', 'unids': 'kg (CH2O)/kg/d', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RML - Relative maintenance respiration rate leaves':
        {'cód': 'RML', 'unids': 'kg(CH2o)/kg/d', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RMO - Relative maintenance respiration rate storage organs':
        {'cód': 'RMO', 'unids': 'kg (CH2O)/kg/d', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'WRT - Dry weight of living roots':
        {'cód': 'WRT', 'unids': 'kg/ha', 'ingr': False, 'egr': True, 'arch': 'result'},
    'WST - Dry weight of living stems':
        {'cód': 'WST', 'unids': 'kg/ha', 'ingr': False, 'egr': True, 'arch': 'result'},
    'WLV - Dry weight of living leaves':
        {'cód': 'WLV', 'unids': 'kg/ha', 'ingr': False, 'egr': True, 'arch': 'result'},
    'WSO - Dry weight of living storage organs':
        {'cód': 'WSO', 'unids': 'kg/ha', 'ingr': False, 'egr': True, 'arch': 'result'},
    'CFET - Correction factor for evapotranspiration in relation to the reference crop':
        {'cód': 'CFET', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DEPNR - Crop group number for soil water depletion':
        {'cód': 'DEPNR', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'IOX - Switch oxygen stress on (1) or off (0)':
        {'cód': 'IOX', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'IAIRDU -Presence of air ducts in roots ':
        {'cód': 'IAIRDU', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'SMCFC - Volumetric soil moisture content at field capacity':
        {'cód': 'SMCFC', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'soil'},
    'RGRLAI - Maximum relative increase in LAI':
        {'cód': 'RGRLAI', 'unids': 'ha/ha/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'SPAN - Life span of leaves growing at 35 ºC':
        {'cód': 'SPAN', 'unids': 'day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TBASE - Lower threshold temperature for ageing of leaves':
        {'cód': 'TBASE', 'unids': 'C', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'PERDL - Maximum relative death rate of leaves due to water stress':
        {'cód': 'PERDL', 'unids': 'kg/kg/d', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'TDWI - Initial total crop dry weight':
        {'cód': 'TDWI', 'unids': 'kg/ha', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'SLATB - Specific leaf area as a function of development stage':
        {'cód': 'SLATB', 'unids': 'ha/kg', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FL - Fraction biomass to leaves':
        {'cód': 'FL', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'FR - Fraction biomass to roots':
        {'cód': 'FR', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'SAI - Stem area index':
        {'cód': 'SAI', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'PAI - Pod area index':
        {'cód': 'PAI', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'TRA - Transpiration rate':
        {'cód': 'TRA', 'unids': 'cm/day', 'ingr': False, 'egr': True, 'arch': 'result'},
    'TRAMX - Maximum transpiration rate':
        {'cód': 'TRAMX', 'unids': 'cm/day', 'ingr': False, 'egr': True, 'arch': 'result'},
    'ADMI - Above-ground dry matter increase':
        {'cód': 'ADMI', 'unids': 'cm/day', 'ingr': False, 'egr': True, 'arch': 'result'},
    'RF_FROST - Reduction factor frost kill':
        {'cód': 'RF_FROST', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'RDI - Initial rooting depth':
        {'cód': 'RDI', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RRI - Maximum daily increase in rooting depth':
        {'cód': 'RRI', 'unids': 'cm/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RDMCR - Maximum rooting depth of mature crop (plant characteristic)':
        {'cód': 'RDMCR', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'RDMSOL - Maximum rooting depth of the soil':
        {'cód': 'RDMSOL', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'soil'},
    'RDRRTB - Relative death rate of roots as a function of development stage':
        {'cód': 'RDRRTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'DMI - Total dry matter increase':
        {'cód': 'DMI', 'unids': 'kg/ha/day', 'ingr': False, 'egr': True, 'arch': 'result'},
    'RDRSTB - Relative death rate of stems as a function of development stage':
        {'cód': 'RDRSTB', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'SSATB - Specific stem area as function of development stage':
        {'cód': 'SSATB', 'unids': 'ha/kg', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FS - Fraction biomass to stems':
        {'cód': 'FS', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'SPA - Specific Pod Area':
        {'cód': 'SPA', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'FO - Fraction biomass to storage organs':
        {'cód': 'FO', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'IDSL - Factor on which development rate between development sSMTABe 0 and 1 depends':
        {'cód': 'IDSL', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'LT50C - Critical LT50 defined as the lowest LT50 value that the wheat cultivar can obtain':
        {'cód': 'LT50C', 'unids': 'C', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_H - Hardening coefficient':
        {'cód': 'FROSTOL_H', 'unids': '1/C/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_D - Dehardening coefficient':
        {'cód': 'FROSTOL_D', 'unids': '1/C3/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_S - Low temperature stress coefficient':
        {'cód': 'FROSTOL_S', 'unids': '1/C/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_R - Respiration stress coefficient':
        {'cód': 'FROSTOL_R', 'unids': '1/day', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_SDBASE - Minimum snow depth for respiration stress':
        {'cód': 'FROSTOL_SDBASE', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_SDMAX - Snow depth with maximum respiration stress':
        {'cód': 'FROSTOL_SDMAX', 'unids': 'cm', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'FROSTOL_KILLCF - Steepness coefficient for logistic kill function':
        {'cód': 'FROSTOL_KILLCF', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'crop'},
    'ISNOWSRC - Use prescribed snow depth from driving variables (0) or modelled snow depth through the kiosk'
    ' (1)':
        {'cód': 'ISNOWSRC', 'unids': 'Dmnl', 'ingr': True, 'egr': False, 'arch': 'site'},
    'TEMP_CROWN - Daily average crown temperature derived from calling the crown_temperature module':
        {'cód': 'TEMP_CROWN', 'unids': 'C', 'ingr': False, 'egr': True, 'arch': 'result'},
    'TMIN_CROWN - Daily minimum crown temperature derived from calling the crown_temperature module':
        {'cód': 'TMIN_CROWN', 'unids': 'C', 'ingr': False, 'egr': True, 'arch': 'result'},
    'ISVERNALISED - Boolean reflecting the vernalisation state of the crop':
        {'cód': 'ISVERNALISED', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'result'},
    'ISNOWSRC - Use prescribed snow depth from driving variables (0) or modelled snow depth through the kiosk'
    '(1)':
        {'cód': 'ISNOWSRC', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'site'},
    'CROWNTMPA - A parameter in equation for crown temperature':
        {'cód': 'CROWNTMPA', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'site'},
    'CROWNTMPB - B parameter in equation for crown temperature':
        {'cód': 'CROWNTMPB', 'unids': 'Dmnl', 'ingr': False, 'egr': True, 'arch': 'site'},
    'SNOWDEPTH - Depth of snow cover':
        {'cód': 'SNOWDEPTH', 'unids': 'cm', 'ingr': False, 'egr': True, 'arch': 'result'},
}

códs_a_vars = dict([(v['cód'], k) for (k, v) in vars_PCSE.items()])

vars_ingreso_PCSE = [v['cód'] for v in vars_PCSE.values() if v['ingr']]

vars_egreso_PCSE = [v['cód'] for v in vars_PCSE.values() if v['egr']]




