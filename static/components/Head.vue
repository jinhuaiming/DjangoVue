<template>
    <div class="h">
    </div>
</template>

<script setup>

/*-- imports --*/
import {
    defineComponent, defineProps,
    onBeforeMount, onMounted, onBeforeUnmount, onUnmounted
} from 'vue';

/*-- 定义组件的名称 --*/
const name = defineComponent({
    name: 'header',
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
/*-- methods --*/
/*-- events --*/
onBeforeMount(() => {
    console.log('Comtext.onBeforeMount');
});
onMounted(() => {
    console.log('Comtext.onBeforeMount');
});
onBeforeUnmount(() => {
    console.log('Comtext.onBeforeUnmount');
});
onUnmounted(() => {
    console.log('Comtext.onUnMounted');
});
</script>


<style scoped>
.h {
    width: 500px;
    height: 100px;
    background-image: url('../static/images/head.png');
    background-size: cover;
    background-position: center;
}
</style>