const {loadModule} = window['vue3-sfc-loader'];
const {defineAsyncComponent} = Vue;

import {CesiumInit} from "./cesiumapis/cesiuminit.js";
import {CesiumLayers} from "./cesiumapis/cesiumlayers.js";
import {CesiumJson} from "./cesiumapis/cesiumjson.js";
/*-- modules --*/
const cesiumapi = {
    CesiumInit: CesiumInit,
    CesiumLayers: CesiumLayers,
    CesiumJson: CesiumJson,
}
/* --stores-- */
/*-- moduleCaches --*/
const moduleCache = {
    "vue": Vue,
    "axios": axios,
    "cesium": cesiumapi,
};

/*-- comoptions --*/
const comoptions = {
    // delimiters: ['[[', ']]',],
    moduleCache: moduleCache, async getFile(url) {
        const res = await fetch(url);
        if (!res.ok) {
            throw Object.assign(new Error(res.statusText + ' ' + url), {res,});
        }
        return {
            getContentData: asBinary => asBinary ? res.arrayBuffer() : res.text()
        };
    }, addStyle(textContent) {
        const style = Object.assign(document.createElement('style'), {textContent,});
        const ref = document.head.getElementsByTagName('style')[0] || null;
        document.head.insertBefore(style, ref);
    },
};

/*-- loadvuecom --*/
function loadVueCOM(vueurl, options = comoptions) {
    return defineAsyncComponent(() => loadModule(vueurl, options));
}

export {loadVueCOM};