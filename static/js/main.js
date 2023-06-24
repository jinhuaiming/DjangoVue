const {createApp} = Vue;
import {loadVueCOM} from "./zero.js";

class ComRoot {
    static begin(rootcomfile) {
        const AppPath = '/static/components/';
        const AppUrl = AppPath + rootcomfile;
        const App = loadVueCOM(AppUrl);
        const app = createApp(App);
        app.use(ElementPlus);
        for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
            app.component(key, component)
        }
        const vueapp = app.mount("#comroot");
    }
}
ComRoot.begin('App.vue');


