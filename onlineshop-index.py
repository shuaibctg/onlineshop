


{% extends "shop/basic.html"%}

{%block css%}
      .col-md-3{
      display: inline-block;
      margin-left: -4px;
      }
      .col-md-3 img{
      width:250px;
      height: 250px;
      }
      body .carousel-indicator li{
      background-color:blue;
      }
      body .carousel-control-prev-icon,
      body .carousel-control-next-icon{
      background-color:blue;
      }
        .carousel-control-prev,
        .carousel-control-next{
        top: auto;
        bottom: auto;
        }
      body .no-padding{
      padding-left:0,
      padding-right:0;
      }
{%endblock%}

{%block body%}
  {%load static %}
<div class="container">
              <!-- SlideShow Starts Here! -->
    {% for product, range, nSlides in allProds %}
    <h5>Flash Sales! {{product.0.category}} - Recommended Items</h5>
    <div id="demo{{forloop.counter}}" class="carousel slide my-3" data-ride="carousel">
      <ul class="carousel-indicators">
        <li data-target="#demo{{forloop.counter}}" data-slide-to="0" class="active"></li>

          {% for i in range%}
        <li data-target="#demo{{forloop.parantloop.counter}}" data-slide-to="{{i}}"></li>
          {% endfor %}
      </ul>


        <div class="container carousel-inner no-padding">
          <div class="carousel-item active">
            <div class="col-xs-3 col-sm-3 col-md-3">
              <div class="card" style="width: 18rem;">
                <img src='/media/{{product.0.image}}' class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{product.0.product_name}}</h5>
                    <p class="card-text">{{product.0.desc}}</p>
                    <button class="btn btn-primary cart">Add To Cart</button>
                </div>
              </div>
            </div>

              {% for i in product|slice:"1:" %}
            <div class="col-xs-3 col-sm-3 col-md-3">
              <div class="card" style="width: 18rem;">
                <img src='/media/{{i.image}}' class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{i.product_name}}</h5>
                    <p class="card-text">{{i.desc}}</p>
                    <button class="btn btn-primary cart">Add To Cart</button>
                </div>
              </div>
            </div>
                {% if forloop.counter|divisibleby:3 and forloop.counter > 0 and not forloop.last %}
            </div><div class="carousel-item">
                {% endif %}
              {% endfor %}
            </div>

          </div>

    </div>


<!-- left right control -->
    <a class="carousel-control-prev" href="#demo{{forloop.counter}}" data-slide="prev">
      <span class="carousel-control-prev-icon"></span>
    </a>

    <a class="carousel-control-next" href="#demo{{forloop.counter}}" data-slide="next">
      <span class="carousel-control-next-icon"></span>
    </a>
{% endfor %}
</div>
{%endblock%}

{% block js%}
<script>
if(localStorage.getItem('cart') == null){
   var cart = {};
}
else{
cart = JSON.parse(localStorage.getItem('cart'));
}

$('.cart').click(function(){
console.log('clicked');
});

    console.log("working");
</script>

{% endblock %}
