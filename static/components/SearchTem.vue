<template>
    <el-drawer v-model="drawer" direction="ltr" :with-header="false">
        <el-scrollbar :height="height">
            <el-link target="_blank" :underline="false" @click="close">
                <el-avatar
                        src="static/images/神奇先生.png" style='background: rgba(0,0,0,0)'
                />
                <h3 style="display: inline-block;font-family: 'Cooper Black';transform: translate(20px,5px)">Argo data
                    retrieval</h3>
            </el-link>
            <el-divider>
                高级检索
            </el-divider>
            <el-form-item label="时间信息：">
                <el-cascader v-model="timeValue" :options="time" placeholder="请选择时间:" clearable/>
            </el-form-item>
            <el-form-item label="图层信息：">
                <el-cascader v-model="layerValue" :options="layer" placeholder="请选择图层:" clearable/>
                <el-button type="primary" icon="Search" style="margin-left: 10px" @click="handerclick">添加</el-button>
            </el-form-item>
        </el-scrollbar>
    </el-drawer>
</template>

<script setup>

/*-- imports --*/
import {
    defineComponent, defineProps, defineExpose, ref,
    onBeforeMount, onMounted, onBeforeUnmount, onUnmounted,
} from 'vue';
import {CesiumLayers} from "cesium";
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
const height = ref('')
const drawer = ref(false)
const timeValue = ref([])
const layerValue = ref([])
const time = ref([
    {
        value: '2022',
        label: '2022年',
        children: [
            {
                value: '01',
                label: '一月'
            },
            {
                value: '02',
                label: '二月'
            },
            {
                value: '03',
                label: '三月'
            },
            {
                value: '04',
                label: '四月'
            },
            {
                value: '05',
                label: '五月'
            },
            {
                value: '06',
                label: '六月'
            },
            {
                value: '07',
                label: '七月'
            },
            {
                value: '08',
                label: '八月'
            },
            {
                value: '09',
                label: '九月'
            },
            {
                value: '10',
                label: '十月'
            },
            {
                value: '11',
                label: '十一月'
            },
            {
                value: '12',
                label: '十二月'
            }

        ],
    },
])
const layer = ref([
    {
        value: 'argoproject',
        label: 'ArgoProject工作空间',
        children: [
            {
                value: 'tem',
                label: '温度',
                children: [
                    {
                        value: '0',
                        label: '0米'
                    },
                    {
                        value: '600',
                        label: '600米'
                    },
                    {
                        value: '1900',
                        label: '1900米'
                    }
                ]
            },


        ],
    },
])

/*-- emit --*/
/*-- methods --*/
const showSearch = (val) => {
    drawer.value = val
}
const close = () => {
    drawer.value = false
}
const handerclick = () => {
    const layerName = layerValue.value[0] + ':' + 'ncfile_' + timeValue.value[0] + "_" + timeValue.value[1] + '_' + layerValue.value[1] + '_' + layerValue.value[2]
    console.log(layerName)
    drawer.value = false
    CesiumLayers.addWMSLayer(props.viewer, 'http://localhost:8080/geoserver/argoproject/wms', layerName)
}
defineExpose({
    showSearch: showSearch
})

/*-- events --*/
// 组件自定义是事件，打开Seach组件
onBeforeMount(() => {
    console.log('Comtext.onBeforeMount');
});
onMounted(() => {
    height.value = (window.outerHeight - 130).toString() + 'px'
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