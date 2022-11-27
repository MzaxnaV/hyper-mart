import 'phaser'

var text;

var counter = { give: 0, take: 0 };

class PlayGame extends Phaser.Scene {
    constructor() {
        super("PlayGame");
    }

    preload() {
        this.load.image('img', '../assets/red.png');
    }

    create() {
        this.add.sprite(0, 600, 'img').setOrigin(0, 1);
        text = this.add.text(10, 10, '', { fill: '#00ff00' });
    }

    update() {
        var pointer = this.input.activePointer;
        this.input.mouse.disableContextMenu();

        var wKey = this.input.keyboard.addKey('W');
        wKey.on('down', function (event) {
            if (counter.give < 1) {
                console.log("TEZOS GIVEN WITH KEYBOARD, W!!!");
            }
            counter.give += 1;
        });
        wKey.on('up', function (event) {
            counter.give = 0;
        });

        var aKey = this.input.keyboard.addKey('A');
        aKey.on('down', function (event) {
            if (counter.take < 1) {
                console.log("TEZOS TAKEN WITH KEYBOARD, A!!!");
            }
            counter.take += 1;
        });
        aKey.on('up', function (event) {
            counter.take = 0;
        });
    }
}

let config = {
    width: 800,
    height: 600,
    parent: 'mygame',
    disableContextMenu: true,
    scene: PlayGame
};

new Phaser.Game(config);