<template>
    <section id="idapp" v-show="visible">
        <Menu @open-search="show_Search" @open-search-tem="show_Search_tem" :viewer="viewer"></Menu>
        <Search :viewer="viewer" ref="drawer"></Search>
        <searchTem :viewer="viewer" ref="drawer_tem"></searchTem>
        <Head class="fixed-top w-50" style="transform: translate(50%)"></Head>
        <div id="map" class="vh-100"></div>
    </section>
</template>

<script setup>

/*-- imports --*/
import {
    defineComponent, defineProps, ref,
    onBeforeMount, onMounted, onBeforeUnmount, onUnmounted
} from 'vue';

import Head from "./Head.vue";
import Search from "./Search.vue";
import SearchTem from "./SearchTem.vue";
import Menu from "./Menu.vue";
import {CesiumInit} from "cesium";


const name = defineComponent({
    name: 'app',
});

/*-- props --*/
const props = defineProps({
    visible: {
        type: String,
        required: false,
        default: 'show',
    },
});
/*-- stores --*/
/*-- vars --*/
const viewer = ref('')
const drawer = ref(null)
const drawer_tem = ref(null)
/*-- methods --*/
const show_Search = (val) => {
    drawer.value.showSearch(val)
}
const show_Search_tem = (val) => {
    drawer_tem.value.showSearch(val)
}
/*-- events --*/
onBeforeMount(() => {

});
onMounted(() => {
    const viewerMap = CesiumInit.init('map');
    viewer.value = viewerMap;
});
onBeforeUnmount(() => {
    console.log('App.onBeforeUnmount');

});
onUnmounted(() => {
    console.log('App.onUnMounted');
});
</script>


<style scoped>

</style>