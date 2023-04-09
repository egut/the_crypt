console.log("Sanity check from index.js.");

// redirect to '/room/<roomSelect>/'
document.querySelector("#roomSelect").onchange = function() {
    let roomName = document.querySelector("#roomSelect").value.split(" (")[0];
    let gameId = document.querySelector("#game_id").value;
    window.location.pathname = "chat/" + gameId + "/" + roomName + "/";
}
