<template>
    <el-space direction="vertical" class="fixed-bottom-left" :size="30">
        <el-tooltip
                class="box-item"
                effect="dark"
                content="全球浮标数据检索"
                placement="right-start"
        >
            <el-button type="primary" icon="Search" @click="$emit('openSearch',true)" circle/>
        </el-tooltip>
        <el-tooltip
                class="box-item"
                effect="dark"
                content="全球海温数据检索"
                placement="right-start"
        >
            <el-button type="info" icon="Ship" @click="$emit('openSearchTem',true)" circle/>
        </el-tooltip>
        <el-tooltip
                class="box-item"
                effect="dark"
                content="全图"
                placement="right-start"
        >
            <el-button type="success" icon="Refresh" @click="fullScene" circle/>
        </el-tooltip>
        <el-tooltip
                class="box-item"
                effect="dark"
                content="Top Left prompts info"
                placement="right-start"
        >
            <el-button type="warning" icon="Star" disabled circle/>
        </el-tooltip>
        <el-tooltip
                class="box-item"
                effect="dark"
                content="Top Left prompts info"
                placement="right-start"
        >
            <el-button type="danger" icon="Delete" disabled circle/>
        </el-tooltip>
    </el-space>
</template>

<script setup>

/*-- imports --*/
import {
    defineComponent, defineProps, defineEmits,
    onBeforeMount, onMounted, onBeforeUnmount, onUnmounted,
} from 'vue';

/*-- 定义组件的名称 --*/
const name = defineComponent({
    name: 'menu',
});

/*-- props --*/
const props = defineProps({
    viewer: {
        type: Object,
        required: true,
        default: null,
    },
});
/*-- stores --*/
/*-- vars --*/
/*-- emits --*/
defineEmits(["openSearch", "openSearchTem"]);
/*-- methods --*/
const fullScene = () => {
    let options = {
        destination: Cesium.Cartesian3.fromDegrees(116, 30, 10000000),
        orientation: {
            heading: Cesium.Math.toRadians(0), // 水平偏角，默认正北 0
            pitch: Cesium.Math.toRadians(-90), // 俯视角，默认-90，垂直向下
            roll: 0, // 旋转角
        },
    };
    props.viewer.camera.flyTo(options);
}
/*-- events --*/
// 组件自定义是事件，打开Seach组件
const openSearch = () => {
    emit('openSearch', true)
}

onBeforeMount(() => {
    console.log('Comtext.onBeforeMount');
});
onMounted(() => {

});
onBeforeUnmount(() => {
    console.log('Comtext.onBeforeUnmount');
});
onUnmounted(() => {
    console.log('Comtext.onUnMounted');
});
</script>

<style scoped>
.fixed-bottom-left {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1030;
    width: 50px;
    transform: translate(5px, -75%);
}
</style>