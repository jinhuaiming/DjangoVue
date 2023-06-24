[TOC]



# 项目背景

​    	杭州全球海洋Argo系统野外科学观测研究站（简称“杭州Argo野外站”），在全球海洋Argo系统（图1）中称“中国Argo实时资料中心（CARDC）”，是在国家科技部基础研究司和国际合作司，以及原国家海洋局科技司、国际合作司、第二海洋研究所和海洋动力过程与卫星海洋学重点实验室等部门、单位的重视和支持下，根据联合国政府间海洋学委员会（IOC）有关Argo计划决议和IOC-WMO（世界气象组织）联合发布的相关函件精神，于2002年4月5日创建并投入试运行；2019年10月29日，正式纳入自然资源部野外科学观测研究站管理序列（自然资办发[2019]45号）。

<img src="http://www.argo.org.cn/uploadfile/image/20200519/1589853987530380.png" alt="图片1.png" style="zoom:80%;" />

杭州Argo野外站主要由海上和陆上两部分组成，其中海上部分是由中国Argo计划布放在全球海洋中的各型自动剖面浮标组成的中国Argo区域海洋观测网，陆上部分则是由北斗卫星导航系统接收天线、服务器、工作站和磁盘阵列，以及Argo数据接收、解码、处理和分发系统等硬软件组成的中国Argo实时资料中心，这也是全球Argo系统中9个业务运行的国家Argo资料中心之一（图2），并在全球Argo资料中心（GDACs）以“CSIO”命名。

野外站具备批量接收和处理多种型号、携带多种传感器的自动剖面浮标观测资料的能力，不仅可以接收利用北斗卫星导航系统定位和传输观测数据的国产剖面浮标，还能接收利用ARGOS、Iridium（铱星）和GPS等卫星定位及传输观测数据的各型国外剖面浮标。其中ARGOS卫星地面接收站位于法国图卢兹，铱卫星接收站位于美国马里兰，而北斗剖面浮标数据服务中心就位于中国杭州，是国际Argo指导组（AST）和国际Argo信息中心（AIC）认可的3个为全球Argo实时海洋观测网提供剖面浮标数据接收服务的国家中心（图2）。

<img src="http://www.argo.org.cn/uploadfile/2020/1106/20201106062316751.png" alt="img" style="zoom: 60%;" />

为了更好的管理Argo野外站和共享数据，建立Argo运营管理系统网络平台，实现实时查看观测站信息。



# 项目设计

## 功能

| 功能         | 描述                                                         |
| ------------ | :----------------------------------------------------------- |
| 查询浮标编号 | 输入浮标平台编号，查询指定平台编号的所有观测周期，并`绘制表格`展示，同时点击绘制按钮，可绘制对应周期的`温盐图`；点击定位按钮可在地图上展示浮标整周期的`移动轨迹线路`。 |
| 添加NC图层   | 选择年份，月份，工作空间，变量类型，深度值，在地图上添加`全球海洋Argo 网格数据集`温度产品。 |







## 技术选型

### 后端

| 所选技术 | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| `Python` | `Python` 是一种解释型、面向对象、动态数据类型的高级程序设计语言 |
| `Django` | `Django` 是一个开放源代码的 Web 应用框架，由 Python 写成。   |

### 前端

| 所选技术          | 描述                                                         |
| :---------------- | ------------------------------------------------------------ |
| `Vue3`            | `Vue3`作为Web 前端框架                                       |
| `ElementPLus`     | 基于 `Vue3`，面向设计师和开发者的组件库                      |
| `vue3-sfc-loader` | 不使用`Create vue`作为脚手架进行前端开发，通过 `CDN` 使用 `Vue` 时，不涉及“`构建步骤`”，这使得设置更加简单，并且可以用于`后端框架`集成。但是无法使用`单文件组件` (SFC) 语法。因此使用 `vue3-sfc-loader`解析`单文件组件`，即可使用单文件组件 (SFC) 语法 |
| `axios`           | `axios`进行前后端通信                                        |
| `Cesium`          | `Cesium`进行地图应用的开发                                   |
| `Echarts`         | `Echarts`展示各种图表数据                                    |

### 数据库

| 所选技术     | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| `PostgreSQL` | `PostgreSQL` 是一款高级的企业级开源关系数据库，支持SQL（关系型）和JSON（非关系型）查询 |



### Web地图服务器

| 所选技术    | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| `GeoServer` | 选用开源服务器`GeoServer`发布各种地图服务，安装`NetCDF`插件，用于后续发布NC文件数据。 |





# 具体实现

## 数据库实现

1. 建立`Argoheader表`，用于储存浮标的每次测量周期有关的数据。

   | Name             | Data Type         | Precision | Scale |
   | ---------------- | ----------------- | --------- | ----- |
   | `platformnumber` | integer           |           |       |
   | `cyclenumber`    | integer           |           |       |
   | `julianday`      | character varying |           |       |
   | `datadate`       | character varying |           |       |
   | `latitude`       | numeric           | 6         | 3     |
   | `longitude`      | numeric           | 6         | 3     |

2. 建立`Argofloat表`，用于储存浮标的每次测量周期有关的数据。

   | Name             | Data Type         | Precision | Scale |
   | ---------------- | ----------------- | --------- | ----- |
   | `platformnumber` |                   |           |       |
   | `cyclenumber`    | integer           |           |       |
   | `lauchdate`      | character varying |           |       |
   | `latitude`       | numeric           | 6         | 3     |
   | `longitude`      | numeric           | 6         | 3     |
   | `projectname`    | character varying |           |       |

3. 建立`Argocore表`，用于储存浮标的每次测量周期有关的数据。

   | Name             | Data Type | Precision | Scale |
   | ---------------- | --------- | --------- | ----- |
   | `platformnumber` | integer   |           |       |
   | `cyclenumber`    | integer   |           |       |
   | `pressure`       | numeric   | 7         | 1     |
   | `cpressure`      | numeric   | 7         | 1     |
   | `qpressure`      | integer   |           |       |
   | `temperature`    | numeric   | 9         | 3     |
   | `ctemperature`   | numeric   | 9         | 3     |
   | `qtemperature`   | integer   |           |       |
   | `salility`       | numeric   | 9         | 3     |
   | `csalility`      | numeric   | 9         | 3     |
   | `qsalility`      | integer   |           |       |



## 前端实现

1. 自定义JavaScript 模块

   | 模块              | 功能                             |
   | ----------------- | -------------------------------- |
   | `cesiumjson.js`   | 封装绘制浮标移动轨迹和绘制温盐图 |
   | `cesiuminit.js`   | 初始化地图空间                   |
   | `cesiumlayers.js` | 封装各种图层的添加方法           |

   

2. Vue组件的实现

   | 组件            |                             功能                             |
   | :-------------- | :----------------------------------------------------------: |
   | `App.vue`       | <img src="C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623160632886.png" alt="image-20230623160632886" style="zoom:20%;" /> |
   | `Head.vue`      | ![image-20230623160025452](D:\windom_hh\DjangoArgo\static\images\head.png) |
   | `Menu.vue`      | <img src="C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623160137161.png" alt="image-20230623160137161" style="zoom:50%;" /> |
   | `Search.vue`    | <img src="C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623160353284.png" alt="image-20230623160353284" style="zoom:25%;" /> |
   | `SearchTem.vue` | <img src="C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623160547170.png" alt="image-20230623160547170" style="zoom:25%;" /> |



## 后端实现

1. `models.py`实现数据库中三张表的转化，对应三个类分别继承于`django.db.models.Model`

   | `类`               | `描述`                     |
   | ------------------ | -------------------------- |
   | `class Argofloat`  | `argofloat`表对应的模型类  |
   | `class Argoheader` | `argoheader`表对应的模型类 |
   | `class Argocore`   | `argocore`表对应的模型类   |

   

2. `view.py`实现`页面渲染`和`创建数据接口API`

   | 函数                       | URL                                     | 描述                                                         |
   | -------------------------- | --------------------------------------- | ------------------------------------------------------------ |
   | `def index(request)`       | http://127.0.0.1:8000/index             | 渲染主页                                                     |
   | `def queryPlaNum(request)` | http://127.0.0.1:8000/index/queryPlaNum | 根据平台标号，查询argoheader表中的完整周期数据和对于的坐标数据，以json格式返回。 |
   | `def handlePlot(request)`  | http://127.0.0.1:8000/index/handlePlot  | 根据平台标号和周期号，查询argocore表中的温度，盐度，深度数据，以json格式返回。 |



# 操作展示

1. 主界面

   ![image-20230623162831212](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623162831212.png)

   

2. 功能1：根据浮标编号，查询数据，绘制温盐图，绘制浮标完成周期移动轨迹。

   - 点击`全球浮标数据检索`按钮

     ![image-20230623163128972](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623163128972.png)

   - 填写浮标编号，点击查询，显示查询的数据，根据周期，点击对应的按钮，可绘制温盐图。

     ![image-20230623163503611](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623163503611.png)

   - 点击`定位`按钮，可查看浮标的移动轨迹

     ![image-20230623163557444](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623163557444.png)

     

3. 功能2：选择年份，月份，工作空间，变量类型，深度值，在地图上添加`全球海洋Argo 网格数据集`温度产品。

   - 点击`全球海温数据检索`按钮

     ![image-20230623163903141](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623163903141.png)

   - 填写年份，月份，工作空间，变量类型，深度值

     ![image-20230623163753534](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623163753534.png)

   - 显示

     ![image-20230623163837762](C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623163837762.png)



# 附件

![图层 3](D:\windom_hh\图层 3.png)

<img src="C:\Users\29298\AppData\Roaming\Typora\typora-user-images\image-20230623164649509.png" alt="image-20230623164649509" style="zoom:50%;" />

## `DjangoArgo/settings.py`

```python
"""
Django settings for DjangoArgo project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0@vd*15s%ug__9s!b7!plz5r*e2=zn+-b(#^r2h#u5a2p(*#$y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'DjangoArgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoArgo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': '127.0.0.1',
        'USER': 'postgres',
        'PASSWORD': 'jinhu19980613',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search-path=public,argo'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / STATIC_URL]
else:
    STATIC_ROOT = STATIC_URL

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```



## `DjangoArgo/urls.py`

```python
"""
URL configuration for DjangoArgo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
]

```



## `myapp/models.py`

```python
from django.db import models


# Create your models here.


class Argofloat(models.Model):
    platformnumber = models.IntegerField(primary_key=True)
    datecenter = models.TextField(blank=True, null=True)
    lauchdate = models.CharField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    projectname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argofloat'
        db_table_comment = '01 Argo-浮标基础信息表'


class Argoheader(models.Model):
    platformnumber = models.IntegerField(
        primary_key=True)  # The composite primary key (platformnumber, cyclenumber) found, that is not supported. The first column is selected.
    cyclenumber = models.IntegerField()
    julianday = models.CharField(blank=True, null=True)
    datadate = models.CharField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argoheader'
        unique_together = (('platformnumber', 'cyclenumber'),)
        db_table_comment = '03 Argo-观测次数信息表'


class Argocore(models.Model):
    platformnumber = models.IntegerField(
        primary_key=True)  # The composite primary key (platformnumber, cyclenumber, pressure) found, that is not supported. The first column is selected.
    cyclenumber = models.IntegerField()
    pressure = models.DecimalField(max_digits=7, decimal_places=1)
    cpressure = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    qpressure = models.CharField(max_length=1, blank=True, null=True)
    temperature = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    ctemperature = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    qtemperature = models.CharField(max_length=1, blank=True, null=True)
    salinity = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    csalinity = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    qsalinity = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argocore'
        unique_together = (('platformnumber', 'cyclenumber', 'pressure'),)
        db_table_comment = '02 Argo-核心数据表'

```

## `myapp/urls.py`

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('queryPlaNum/', views.queryPlaNum, name='queryPlaNum'),
    path('handlePlot/', views.handlePlot, name='handlePlot'),
}

```

## `myapp/views.py`

```python
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from .models import Argoheader, Argocore
import json


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

# 根据浮标编号，查询浮标的所有周期信息
def queryPlaNum(request):
    platformnumber = request.GET.get('platformnumber')
    data = Argoheader.objects.filter(platformnumber=platformnumber)
    data_json = json.loads(serializers.serialize('json', data))
    position = []
    for item in data_json:
        position.append(item['fields']['longitude'])
        position.append(item['fields']['latitude'])
    position_data = [
        {platformnumber: position}
    ]
    return JsonResponse({
        'data': data_json,
        'position': position_data
    })

# 根据浮标编号和周期号，查询浮标某周期，测量的温度|盐度的数值
def handlePlot(request):
    pk = request.GET.get('pk')
    cyclenumber = request.GET.get('cyclenumber')
    data = Argocore.objects.filter(platformnumber=pk, cyclenumber=cyclenumber)
    data_json = json.loads(serializers.serialize('json', data))
    Depth = []
    Tem = []
    Sal = []
    for item in data_json:
        Depth.append(item['fields']['cpressure'])
        Tem.append(item['fields']['ctemperature'])
        Sal.append(item['fields']['csalinity'])
    Depth = Depth[::-1]
    Tem = Tem[::-1]
    Sal = Sal[::-1]

    return JsonResponse({
        'data': {
            'Depth': Depth,
            'Tem': Tem,
            'Sal': Sal
        }
    })


```

## `static/components.App.vue`

```vue
/<template>
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
```

## `static/components.Head.vue`

```vue
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
```

## `static/components.Menu.vue`

```vue
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
```

## `static/components.Menu.vue`

```vue
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
```

## `static/components.Search.vue`

```vue
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
```

## `static/js/cesiumapis/cesiuminit.js`

```js
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
```

## `static/js/cesiumapis/cesiumjson.js`

```js
class CesiumJson {
    // 根据数据库查询的Argo浮标整个周期，绘制浮标移动轨迹。
    static addPolyline(viewer, json) {
        // json = [
        //     {1983123: [lon,lat,....],
        // ]
        
        const data = Object.entries(json[0])[0]
        const platformnumber = data[0]
        const positions = data[1]
        // 绘制移动轨迹
        const entity = viewer.entities.add({
            polyline: {
                id: platformnumber,
                positions: Cesium.Cartesian3.fromDegreesArray(positions),
                width: 5,
                clampToGround: true,
                // material: getCustomMaterialLine(MaterialLineImage, colors),
                material: Cesium.Color.BLUE,
            }
        });
        // 移动到浮标视角
        viewer.flyTo(entity, {
            duration: 3,
        });
        return entity;
        // 删除绘制的移动轨迹
        // viewer.entities.remove(entity);
    }

    // 根据数据库查询的Argo某个浮标某次完整周期，绘制温盐图。
    static drawTemSal(depth, temperature, salinity) {
        // 初始化一次即可，需要优化!
        const myChart = echarts.init(document.getElementById('plot'));
        var option = {
            legend: {
                data: ['temperature(°C)', 'salinity(‰)'],
            },
            tooltip: {
                trigger: 'axis'
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'value',
                axisLabel: {
                    formatter: '{value} °C/‰'
                }
            },
            yAxis: {
                type: 'category',
                axisLine: {onZero: false},
                axisLabel: {
                    formatter: '{value}m'
                },
                boundaryGap: false,
                // 深度值
                data: depth
            },
            series: [
                {
                    name: 'temperature(°C)',
                    type: 'line',
                    symbolSize: 8,
                    symbol: 'circle',
                    smooth: true,
                    lineStyle: {
                        width: 2,
                        shadowColor: 'rgba(0,0,0,0.3)',
                        shadowBlur: 10,
                        shadowOffsetY: 8
                    },
                    // 温度值
                    data: temperature
                },
                {
                    name: 'salinity(‰)',
                    type: 'line',
                    symbolSize: 8,
                    symbol: 'circle',
                    smooth: true,
                    lineStyle: {
                        width: 2,
                        shadowColor: 'rgba(0,0,0,0.3)',
                        shadowBlur: 10,
                        shadowOffsetY: 8
                    },
                    // 盐度值
                    data: salinity
                }
            ]
        };
        myChart.setOption(option);
    }
}

export {CesiumJson};
```

## `static/js/cesiumapis/cesiumlayers.js`

```js
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

```

## `static/js/main.js`

```js
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



```

## `static/js/zero.js`

```js
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
```

## `templates/app/base_index.html`

```django
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <link rel="shortcut icon" href="/static/images/神奇先生.ico" type="image/x-icon">
    <link rel="stylesheet" href="/static/libs/bootstrap/css/bootstrap.css">
    <link rel="stylesheet" href="/static/libs/cesium/Widgets/widgets.css">
    <link rel="stylesheet" href="/static/libs/elementplus/index.css">

    <script src="/static/libs/cesium/Cesium.js"></script>
    <script src="/static/js/cesiumapis/cesium-materialLine.js"></script>
    <script src="/static/libs/bootstrap/js/bootstrap.min.js"></script>
    <script src="/static/libs/axios/axios.min.js"></script>
    <script src="/static/libs/vue/vue.global.prod.js"></script>
    <script src="/static/libs/vue3-sfc-loader/vue3-sfc-loader.js"></script>
    <script src="/static/libs/elementplus/index.js"></script>
    <script src="/static/libs/echarts/echarts.js"></script>
    <script src="/static/libs/elementplus/element-plus_icons-vue.js"></script>

    {% block css %}

    {% endblock %}
    <title>Argo浮标运营管理系统</title>
</head>
<body>
<main id="comroot">
    {% block body %}

    {% endblock %}
</main>
{% block script %}

{% endblock %}
</body>
</html>
```

## `templates/app/index.html`

```django
{% extends 'app/base_index.html' %}

{#style#}
{% block css %}
    <link rel="stylesheet" href="/static/css/index.css">
{% endblock %}


{#body#}
{% block body %}

{% endblock %}

{#script#}
{% block script %}
    <script src="/static/js/main.js" type="module"></script>
{% endblock %}
```

