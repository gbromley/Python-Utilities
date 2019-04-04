def plot_ngp_4seasons(lat, lon, var,pvals,levs,extent,colormp='RdBu_r',path_to_shape='/Users/gbromley/Dropbox/Montana_Climate_Project/Study_Area/Study_Area_08_01_17.shp', out_path='/Users/gbromley/Dropbox/Montana_Climate_Project/Model_paper/Figures/figure_new.png'){

#np.linspace(cb_min, cb_max, len(cus_col))
    #create figure

    #np.linspace(cb_min, cb_max, len(cus_col))
    fig = plt.figure(1,figsize=(13,7), dpi=400.0)
    #create projection
    projection = ccrs.LambertConformal(central_longitude=-105,central_latitude=45,standard_parallels=[50,40])
    ax1 = plt.subplot(2,2,1, projection = projection)

    cb = plt.contourf(lon,lat,var,transform=ccrs.PlateCarree(),levels=levs,cmap=colormp, extend='both')
    pvals[0,:,:].plot.contourf(axes=ax1,transform=ccrs.PlateCarree(),color='none',edgecolor='black',hatches=["..."],alpha=0.,add_colorbar = False)
    ax1.set_extent(extent)
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    ax1.add_feature(states_provinces, edgecolor='lightgray')
    ax1.add_feature(cfeature.COASTLINE)
    ax1.add_feature(cfeature.BORDERS)
    shape_feature = ShapelyFeature(Reader(path_to_shape).geometries(),crs=ccrs.PlateCarree(), facecolor='none',edgecolor='black')
    ax1.add_feature(shape_feature)
    ax1.title.set_text('DJF')
    at = AnchoredText("a",
                      prop=dict(size=8), frameon=True,
                      loc=2,
                      #backgroundcolor = 'lightgray'
                      )
    ax1.add_artist(at)

    ax2 = plt.subplot(2,2,2, projection = projection)

    plt.contourf(spatial_trend.lon,spatial_trend.lat,spatial_trend[2,:,:].values,transform=ccrs.PlateCarree(),levels=levs,cmap=colormp, extend='both')
    pvals[2,:,:].plot.contourf(axes=ax1,transform=ccrs.PlateCarree(),color='none',edgecolor='black',hatches=["..."],alpha=0.,add_colorbar = False)

    ax2.set_extent(extent)
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    ax2.add_feature(states_provinces, edgecolor='lightgray')
    ax2.add_feature(cfeature.COASTLINE)
    ax2.add_feature(cfeature.BORDERS)
    ax2.add_feature(shape_feature)
    bt = AnchoredText("b",
                      prop=dict(size=8), frameon=True,
                      loc=2,
                      #backgroundcolor = 'lightgray'
                      )
    ax2.add_artist(bt)
    ax2.set_title('MAM')
    #ax2.title.set_visible(False)

    ax3 = plt.subplot(2,2,3, projection = projection)

    plt.contourf(spatial_trend.lon,spatial_trend.lat,spatial_trend[1,:,:].values,transform=ccrs.PlateCarree(),levels=levs,cmap=colormp, extend='both')
    #ax = plt.axes(projection=ccrs.LambertConformal())
    pvals[1,:,:].plot.contourf(axes=ax1,transform=ccrs.PlateCarree(),color='none',edgecolor='black',hatches=["..."],alpha=0.,add_colorbar = False)

    ax3.set_extent(extent)
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    ax3.add_feature(states_provinces, edgecolor='lightgray')
    ax3.add_feature(cfeature.COASTLINE)
    ax3.add_feature(cfeature.BORDERS)
    ax3.add_feature(shape_feature)
    ct = AnchoredText("c",
                      prop=dict(size=8), frameon=True,
                      loc=2,
                      #backgroundcolor = 'lightgray'
                      )
    ax3.add_artist(ct)
    ax3.set_title('JJA')

    ax4 = plt.subplot(2,2,4, projection = projection)

    plt.contourf(spatial_trend.lon,spatial_trend.lat,spatial_trend[3,:,:].values,transform=ccrs.PlateCarree(),levels=levs,cmap=colormp, extend='both')
    #ax = plt.axes(projection=ccrs.LambertConformal())
    pvals[3,:,:].plot.contourf(axes=ax1,transform=ccrs.PlateCarree(),color='none',edgecolor='black',hatches=["..."],alpha=0.,add_colorbar = False)
    ax4.set_extent(extent)
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    ax4.add_feature(states_provinces, edgecolor='lightgray')
    ax4.add_feature(cfeature.COASTLINE)
    ax4.add_feature(cfeature.BORDERS)
    ax4.add_feature(shape_feature)
    dt = AnchoredText("d",
                      prop=dict(size=8), frameon=True,
                      loc=2,
                      #backgroundcolor = 'lightgray'
                      )
    ax4.add_artist(dt)
    ax4.set_title('SON')
    fig.subplots_adjust(top=0.9,bottom=0.1,left=0.25,right=0.75,hspace=0.1,wspace=0.1)
    fig.suptitle('Temperature Trends 1970-2015')
    cax = fig.add_axes((0.76, 0.12, 0.03, 0.76))
    col_bar = fig.colorbar(cb,cax=cax)
    col_bar.set_label('$^\circ$C / Decade',fontsize=10)

    #plt.tight_layout()
    plt.savefig(out_path),bbox_inches='tight')
    plt.show()
}
