import '../static'

const product = [
    {
        id: 0,
        image: '../static/imagenes/prote1.png',
        title: 'WHEY PROTEIN FRUTOS DEL BOSQUE 300G',
        price: 23000,
    },
    {
        id: 1,
        image: '../imagenes/prote2.png',
        title: 'WHEY PROTEIN GOLD 300G',
        price: 27000,
    },
    {
        id: 2,
        image: '../imagenes/prote3.png',
        title: 'FIB0 PROTEIN BARS X12',
        price: 27000,
    },
    {
        id: 3,
        image: '../imagenes/creatina1.png',
        title: 'DRIVE CREATINE 300G',
        price: 25000,
    },
    {
        id: 4,
        image: '../imagenes/creatina2.png',
        title: 'RC CREATINE 300G',
        price: 29000,
    },
    {
        id: 5,
        image: '../imagenes/creatina3.png',
        title: 'W1 CREATINE 300G',
        price: 28000,
    }
];
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price} CLP</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Agregar al carro</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Tu carrito esta vacío";
        document.getElementById("total").innerHTML = "$ "+0+" CLP";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "$ "+total+" CLP";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>$ ${price}  CLP</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}
