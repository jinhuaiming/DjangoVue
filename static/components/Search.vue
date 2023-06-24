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
            <el-input
                    class="w-75"
                    v-model="input"
                    placeholder="平台编号(默写查询编号-19019):"
                    prefix-icon="Search"
                    clearable
            />
            <el-button type="primary" icon="Search" @click="handelClick" circle style="margin-left: 10px"/>
            <el-button type="danger" icon="LocationInformation" @click="handelClickPosition" circle
                       :disabled="disable"/>
            <el-divider>
                查询结果
            </el-divider>
            <el-table :data="tableData" height="300" style="width: 100%">
                <el-table-column type="expand">
                    <template #default="props">
                        <el-descriptions title="浮标基础信息" size="small" column="1">
                            <el-descriptions-item label="采样日期">
                                <el-tag size="small">{{ props.row.fields.datadate }}</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="儒略历">
                                <el-tag size="small">{{ props.row.fields.julianday }}</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="纬度">
                                <el-tag size="small">{{ props.row.fields.latitude }}</el-tag>
                            </el-descriptions-item>
                            <el-descriptions-item label="经度">
                                <el-tag size="small">{{ props.row.fields.longitude }}</el-tag>
                            </el-descriptions-item>

                        </el-descriptions>
                    </template>
                </el-table-column>
                <el-table-column label="平台编号" prop="pk"/>
                <el-table-column label="周期" prop="fields.cyclenumber"/>
                <el-table-column label="绘图" align="right">
                    <template #default="scope">
                        <el-button
                                size="small"
                                type="danger"
                                icon="PieChart"
                                circle
                                @click="handlePlot(scope.row.pk,scope.row.fields.cyclenumber)"
                        >
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <el-divider>
                Argo{{ platformnumber }}-{{ cyclenumber1 }}-温盐图
            </el-divider>
            <div id='plot' style="min-height: 400px;"></div>
        </el-scrollbar>
    </el-drawer>
</template>
<script setup>

/*-- imports --*/
import {
    defineComponent, defineProps, defineExpose,
    onBeforeMount, onMounted, onBeforeUnmount, onUnmounted,
    ref
} from 'vue';
// 会导致加载和刷新变慢
// import {ElNotification} from '../libs/elementplus/index.js'
import {CesiumJson} from 'cesium'
/*-- 定义组件的名称 --*/
const name = defineComponent({
    name: 'left',
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
const drawer = ref(false)
const input = ref('19019')
const tableData = ref()
const height = ref('500px')
const platformnumber = ref('19019')
const cyclenumber1 = ref('129')
const disable = ref(true)
var positonData = Object
/*-- methods --*/
const showSearch = (val) => {
    drawer.value = val
}
const close = () => {
    drawer.value = false
}
/*-- Expose --*/
defineExpose({
    showSearch: showSearch
})
// 绘制温度盐度曲线
const handlePlot = (pk, clcyenumber) => {
    axios.get('/handlePlot', {
        params: {
            pk: pk,
            cyclenumber: clcyenumber
        }
    })
        .then(function (response) {
            const depth = response.data.data.Depth;
            const tem = response.data.data.Tem;
            const sal = response.data.data.Sal;
            platformnumber.value = pk;
            cyclenumber1.value = clcyenumber;
            CesiumJson.drawTemSal(depth, tem, sal);
        })
        .catch(function (error) {
            // ElNotification({
            //     title: '警告',
            //     message: error,
            //     type: 'warning',
            //     duration: 2000
            // })
        })
}
// 查询指定浮标编号的所有
const handelClick = () => {
    axios.get('/queryPlaNum', {
        params: {
            platformnumber: input.value
        }
    })
        .then(function (response) {
            if (response.data.data.length === 0) {
                disable.value = true
                // ElNotification({
                //     title: '警告',
                //     message: '浮标不存在，请重新输入！',
                //     type: 'warning',
                //     position: 'top-left',
                //     duration: 1000
                // })
            } else {
                tableData.value = response.data.data;
                positonData = response.data.position
                disable.value = false
            }

        })
        .catch(function (error) {
            // ElNotification({
            //     title: '警告',
            //     message: error,
            //     type: 'warning',
            //     duration: 2000
            // })
            disable.value = true
        })
}

const handelClickPosition = () => {
    drawer.value = false
    CesiumJson.addPolyline(props.viewer, positonData)
}

/*-- events --*/
onBeforeMount(() => {
    console.log('Comtext.onBeforeMount');
});
onMounted(() => {
    // var myChart = echarts.init(document.getElementById('plot'));
    // 设置滚轮高度
    height.value = (window.outerHeight - 130).toString() + 'px'
    // 查询浮标信息
    handelClick()
    // 绘制浮标的温盐图
    handlePlot('19019', '129')
    // 情况输入框的数值
    input.value = ''
    // 初始化绘图对象
});
onBeforeUnmount(() => {
    console.log('Comtext.onBeforeUnmount');
});
onUnmounted(() => {
    console.log('Comtext.onUnMounted');
});
</script>
<style scoped>

</style>