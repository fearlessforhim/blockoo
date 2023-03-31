Vue.component('VueRow',
    {
        name: 'VueRow',
        props: {
            rowList: {
                type: Array,
                required: true
            }
        },
        delimiters: ['[[', ']]'],
        data() {
            return {
            }
        },
        methods: {
            handleClick(x, y){
                this.$emit('cellclick', {x: x, y: y})
            }
        }
    });