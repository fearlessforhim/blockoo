new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        grid: [],
        selectedPiece: 'NSN',
        activeColor: 'red',
        rotationMod: 0,
        isMirrored: false,
        players: [],
        currentPlayerId: 0,
        selectedPlayerPiece: {
            pieceKey: '',
            playerColor: ''
        }
    },
    async created() {
        this.loadGrid();

        this.loadPlayers();
    },
    methods: {
        handleCellClicked(data) {
            console.log('handlecellclicked');
            console.log(data);
            this.doPost(data.x, data.y);
        },
        handlePieceSelected(data) {
            this.selectedPlayerPiece = data;
            this.activeColor = data.playerColor;
            this.selectedPiece = data.pieceKey;
        },
        getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },
        async init() {
            let result = await axios({
                method: "POST",
                url: 'init'
            });
            console.log(result.data.message)
            this.loadGrid();
            this.loadPlayers();
        },
        async loadGrid() {
            let result = await axios({
                method: "GET",
                url: 'getState'
            });
            this.grid = result.data;
        },
        async loadPlayers() {
            let result = await axios({
                method: "GET",
                url: 'players'
            });

            console.log(result.data);

            this.players = result.data['playerArray'];
            this.players.forEach((p) => {
                let stringArr = p.remainingPieces.split(",");
                let remainingPieces = [];
                stringArr.forEach((a) => {
                    remainingPieces.push({
                        selected: false,
                        key: a
                    })
                });
                this.$set(p, 'remainingPieces', remainingPieces);
            });
            this.currentPlayerId = result.data['currentPlayer'];
        },
        async doPost(xCoord, yCoord) {
            var csrftoken = this.getCookie('csrftoken');
            let result = await axios({
                method: "POST",
                url: 'placePiece',
                data: {
                    'xCoord': xCoord,
                    'yCoord': yCoord,
                    'color': this.activeColor,
                    'piece': this.selectedPiece,
                    'rotationModifier': this.rotationMod,
                    'isMirrored': this.isMirrored,
                    'csrfmiddlewaretoken': csrftoken
                }
            });
            if (result.data.message) {
                console.log(result.data.message)
            } else {
                this.grid = result.data;
                this.loadPlayers();
                this.isMirrored = false;
                this.rotationMod = 0;
            }
        },
        async passPlayer() {
            let result = await axios({
                method: "POST",
                url: 'passPlayer'
            });
            this.loadPlayers();
        },
        rotateRight() {
            this.rotationMod += 1;
            if (this.rotationMod > 3)
                this.rotationMod = 0;
            console.log(this.rotationMod)
        },
        rotateLeft() {
            this.rotationMod -= 1;
            if (this.rotationMod < 0)
                this.rotationMod = 3;
            console.log(this.rotationMod)
        },
        setMirrored() {
            this.isMirrored = !this.isMirrored;
            console.log(this.isMirrored)
        }
    },
    computed: {
        currentPlayerName() {
            if (this.currentPlayerId === 1)
                return "Blue";
            else if (this.currentPlayerId === 2)
                return "Yellow";
            else if (this.currentPlayerId === 3)
                return "Green";
            else
                return "Red";
        }
    }
});