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