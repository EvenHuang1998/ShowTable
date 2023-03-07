<template>
    <div>
        <a-table :columns="columns" :data-source="table_data" :pagination="false"  bordered>
        </a-table>
    </div>
</template>

<script>
const columns = [
  {
    title: 'rank',
    dataIndex: 'rank',
    width: '15%',
    scopedSlots: { customRender: 'columns' },
  },
  {
    title: 'flow',
    dataIndex: 'flow',
    width: '70%',
    scopedSlots: { customRender: 'flow' },
  },
  {
    title: 'count',
    dataIndex: 'count',
    width: '15%',
    scopedSlots: { customRender: 'count' },
  },
];

export default {
    name: "ShowTable",
    data() {
        return {
            table_data:[],
            columns
        };
    },
    sockets:{
        updateTable(val){
            console.log(val);
        },
    }
};
</script>

<style scoped>
</style>