Vue.component('PlayerControl',
    {
        name: 'PlayerControl',
        props: {
            players: {
                type: Array,
                required: true
            },
            rotationMod: {
                type: Number,
                required: true
            },
            isMirrored: {
                type: Boolean,
                required: true
            },
            selectedPiece: {
                type: Object,
                required: true
            }
        },
        delimiters: ['[[', ']]'],
        data() {
            return {
            }
        },
        methods: {
            handlePieceSelected(data) {
                this.$emit('pieceselected', {pieceKey: data.pieceKey, playerColor: data.playerColor})
            }
        }
    });