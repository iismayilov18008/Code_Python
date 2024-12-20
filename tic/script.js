const cells = document.querySelectorAll('.cell')
const popup = document.querySelector('.popup')
const winDiv = document.querySelector('.winDiv')
const winText = document.querySelector('.winText')
const restart = document.querySelector('#restart')
let player = 'x'
let gameStep = 0

let gameArr = [
    ['','',''],
    ['','',''],
    ['','',''],
]


function checkWin(player) {
    // Check rows
    for (let row = 0; row < 3; row++) {
        if (gameArr[row][0] === player && gameArr[row][1] === player && gameArr[row][2] === player) {
            return true; 
        }
    }

    // Check columns
    for (let col = 0; col < 3; col++) {
        if (gameArr[0][col] === player && gameArr[1][col] === player && gameArr[2][col] === player) {
            return true;  
        }
    }

    // Check diagonals
    if (gameArr[0][0] === player && gameArr[1][1] === player && gameArr[2][2] === player) {
        return true; 
    }
    if (gameArr[0][2] === player && gameArr[1][1] === player && gameArr[2][0] === player) {
        return true; 
    }

    return false;
}



function restartGame() {
    player = 'x'
    gameArr = [
        ['','',''],
        ['','',''],
        ['','',''],
    ]
    gameStep = 0

    cells.forEach(c => {
        c.innerText = ''
    })

    winDiv.style.display = "none"

}


function startGame() {


    restart.addEventListener('click', ()=>{
        restartGame()
    })


    cells.forEach(c => {
        c.addEventListener('click', () => {
            if (c.innerText==='x' || c.innerText==='o') {
                popup.style.left = '10px'
                setInterval(()=>{
                    popup.style.left = '-1000px'
                }, 1500)
            } else {
                c.innerText = player
                const row = c.getAttribute('cell-row')
                const col = c.getAttribute('cell-col')
                gameArr[row][col] = player

                if (checkWin(player)) {
                    winText.innerText = `Player ${player.toUpperCase()} Won!`
                    winDiv.style.display = "flex"
                }
                gameStep++
                if (gameStep>=9) {
                    winText.innerText = `Draw!`
                    winDiv.style.display = "flex"
                }
                player = player==='x' ? 'o' : 'x'
            }
        })
    });
}


startGame()