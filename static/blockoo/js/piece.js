Vue.component('Piece',
    {
        name: 'Piece',
        props: {
            pieceKey: {
                type: String,
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
            playerColor: {
                type: String,
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
        created() {
        },
        methods: {
            handlePieceSelection(){
                this.selected = true;
                this.$emit('pieceselected', {pieceKey: this.pieceKey, playerColor: this.playerColor})
            }
        },
        computed: {
            rotationClass() {
                if (this.rotationMod === 1)
                    return "ninety";
                else if (this.rotationMod === 2)
                    return "oneEighty";
                else if (this.rotationMod === 3)
                    return "twoSeventy";
                else
                    return "";
            },
            selected() {
                return this.selectedPiece.pieceKey === this.pieceKey && this.selectedPiece.playerColor === this.playerColor;
            }
        }
    })
;