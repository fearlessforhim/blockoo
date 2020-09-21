Vue.component('PieceRow',
    {
        name: 'PieceRow',
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
        }
    });