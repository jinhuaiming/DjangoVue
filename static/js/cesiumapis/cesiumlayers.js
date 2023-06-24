class CesiumLayers {
    static addWMSLayer(viewer, url, layers) {
        const provider = new Cesium.WebMapServiceImageryProvider({
            url: url,
            layers: layers,
            parameters: {
                transparent: true,     //是否透明
                format: 'image/png',
                // srs: 'EPSG:4326'
            }
        });
        viewer.imageryLayers.addImageryProvider(provider);
        if (viewer.imageryLayers.length > 2) {
            // 删除上一次添加的影响
            viewer.imageryLayers.remove(viewer.imageryLayers.get(1))
        }
    }

    static addTDLayer(viewer) {
        const tdtImageryProvider = new Cesium.WebMapTileServiceImageryProvider({
            url: 'http://t0.tianditu.gov.cn/vec_w/wmts?tk=pk.eyJ1Ijoid2ViZ2lzNGRlbHBoaSIsImEiOiJjbGRiN3doMDMwcWZkM3lsaWdqM2xva3d4In0.d9v0S4tp2APHFLXirNecpw', // 天地图影像底图服务地址
            layer: 'image', // 影像图层
            style: 'image/jpeg', // 默认样式
            format: 'tiles', // 切片格式
            tileMatrixSetID: 'w', // 切片矩阵集标识符
            maximumLevel: 18, // 最大级别
            credit: '天地图' // 底图来源标识
        });
        viewer.imageryLayers.addImageryProvider(tdtImageryProvider);
        return viewer.imageryLayers.length;
    }

}


export {CesiumLayers};
