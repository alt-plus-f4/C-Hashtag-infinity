function onSearch(event){
    event.preventDefault();
    text = document.getElementById('src-form').value;
    let url = "http://192.168.100.19:5000/articles?search=" + text
    //et url = "https://www.nasa.gov/api/2/ubernode/477611"
    console.log(text._id);

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(xmlHttp.responseText);
}

var canvasDots = function() {
    var canvas = document.querySelector('canvas'),
        ctx = canvas.getContext('2d'),
        colorDot = '#FFFFFF',
        color = '#FFFFFF';
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    canvas.style.display = 'block';
    ctx.fillStyle = colorDot;
    ctx.lineWidth = .1;
    ctx.strokeStyle = color;

    var mousePosition = {
        x: 30 * canvas.width / 100,
        y: 30 * canvas.height / 100
    };

    var dots = {
        nb: innerWidth * 0.3,
        distance: 45,
        d_radius: 50,
        array: []
    };

    function Dot(){
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;

        this.vx = -.5 + Math.random();
        this.vy = -.5 + Math.random();

        this.radius = Math.random();
    }

    Dot.prototype = {
        create: function(){
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
            ctx.fill();
        },

        animate: function(){
            for(i = 0; i < dots.nb; i++){

                var dot = dots.array[i];

                if(dot.y < 0 || dot.y > canvas.height){
                    dot.vx = dot.vx;
                    dot.vy = - dot.vy;
                }
                else if(dot.x < 0 || dot.x > canvas.width){
                    dot.vx = - dot.vx;
                    dot.vy = dot.vy;
                }
                dot.x += dot.vx;
                dot.y += dot.vy;
            }
        },

        line: function(){
            for(i = 0; i < dots.nb; i++){
                for(j = 0; j < dots.nb; j++){
                    i_dot = dots.array[i];
                    j_dot = dots.array[j];

                    if((i_dot.x - j_dot.x) < dots.distance && (i_dot.y - j_dot.y) < dots.distance && (i_dot.x - j_dot.x) > - dots.distance && (i_dot.y - j_dot.y) > - dots.distance){
                        if((i_dot.x - mousePosition.x) < dots.d_radius && (i_dot.y - mousePosition.y) < dots.d_radius && (i_dot.x - mousePosition.x) > - dots.d_radius && (i_dot.y - mousePosition.y) > - dots.d_radius){
                            ctx.beginPath();
                            ctx.moveTo(i_dot.x, i_dot.y);
                            ctx.lineTo(j_dot.x, j_dot.y);
                            ctx.stroke();
                            ctx.closePath();
                        }
                    }
                }
            }
        }
    };

    function createDots(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for(i = 0; i < dots.nb; i++){
            dots.array.push(new Dot());
            dot = dots.array[i];

            dot.create();
        }

        dot.line();
        dot.animate();
    }

    window.onmousemove = function(parameter) {
        mousePosition.x = parameter.pageX;
        mousePosition.y = parameter.pageY;
    }

    mousePosition.x = window.innerWidth / 2;
    mousePosition.y = window.innerHeight / 2;

    setInterval(createDots, 1000/30);
};

window.onload = function() {
    canvasDots();
    const form = document.getElementById('search-form');
    form.addEventListener("submit", onSearch)

    var images = ["https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/potw2103a.jpg", "https://www.cloudynights.com/uploads/monthly_09_2017/post-201437-0-79335000-1506796278.jpg", "https://i.stack.imgur.com/wIfpv.jpg", "https://i.stack.imgur.com/TZCPl.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSw1EG-08-l26oBJVw6bHZJ66q2JTxStvB_Q&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3mCqC4yDgDpedCkublsTJogJJpqGe3eFDaQ&usqp=CAU", "https://ak.picdn.net/shutterstock/videos/6966808/thumb/1.jpg?ip=x480", "https://wallpaperaccess.com/full/4423937.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-pVSXogwo_Z-pRzRoug6m_rsXlzPsSRuxpQ&usqp=CAU", "https://images.wisegeek.com/slideshow-mobile-small/planet-mars-in-space.jpg", "https://i.imgur.com/1Ul1TMZ.jpeg", "https://i.imgur.com/MRoS1qN.jpeg", "https://i.imgur.com/50VjiqY.jpeg", "https://i.imgur.com/3Yjs9zY.jpeg", "https://i.imgur.com/nCMk2n9.jpeg"]
    for (let i = 0; i < images.length; i++) {
        document.getElementById("i", i).style.backgroundImage = url(images[Math.floor(Math.random * images.length)].toString())
        console.log("test")
    }


};


