class CesiumInit {
    static init(container) {
        const viewer = new Cesium.Viewer(container, {
            timeline: false,
            animation: false,
            baseLayerPicker: false,
            navigationHelpButton: false,
            fullscreenButton:false,
            sceneModePicker: false,
            selectionIndicator: false,
            geocoder: false
        })
        return viewer;
    }
}

export {CesiumInit};