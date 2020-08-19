<template>
    <div class="fondo">       
        <section class="fondo1" :style= "{ backgroundImage: 'url(' + require('@/assets/inventeye0.jpg') + ')' }">
                <navbar_dl></navbar_dl>
            <div class="container2ie" >
                <h1 class="inventeye-title">{{tituloArticulo}}</h1>
            </div>
        </section>
        <section :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
            <div class="container1" >
            </div>
        </section>
        
        <div class="frame-classic">
            <articuloIzqFrame  
                v-bind:tituloArticulo= "title0" 
                v-bind:textoArticulo= "article0" 
                v-bind:textoSobreImagen= "textimg0"
                v-bind:imagenConGamma= "imagenConGamma0"
                v-bind:imagenFondo= "imagenFondo0"
            />
        </div>

        <div class="frame-classic">
        <articuloFrame  
            v-bind:tituloArticulo= "title1" 
            v-bind:textoArticulo= "article1" 
            v-bind:textoSobreImagen= "textimg1"
            v-bind:imagenConGamma= "imagenConGamma1"
            v-bind:imagenFondo= "imagenFondo1"
        />
        </div>
        <lowerBanner />
    </div>
</template>

<script>
//import Parallax from "vue-parallaxy";
import navbar_dl from '@/components/page_web/ListNavbar.vue';
import articuloFrame from '@/components/ArticuloFrame/ArticuloFrame.vue';
import articuloIzqFrame from '@/components/ArticuloFrame/ArticuloIzqFrame.vue';
import articuloIzqFrameColor from '@/components/ArticuloFrame/ArticuloIzqFrameColor.vue';
import lowerBanner from '@/components/ArticuloFrame/LowerBanner.vue';
export default {
  name: 'paralax_dl',
  components: {
    navbar_dl,
    articuloIzqFrame,
    articuloFrame,
    lowerBanner
  },
  props: {
      tituloArticulo:{
        type: String,
        default:"INVENTEYE"
      },
  },
  data(){
    return {     
      title0:'Inventarios basados en imagenes.',
      article0:'Por medio del uso de sensores y algoritmos de reconocimiento'+
                ' realizamos inventarios de maquinaria y equipo de difícil '+
                'acceso como también inventario de bodega.',
      textimg0: 'InventEye',
      imagenConGamma0:"Servicios.png",
      imagenFondo0:"inventeye2.png",


      title1:'Usos',
      article1:'Generar inventarios de material y equipo en tiempo record basádondonos  en ímagenes.',

      textimg1: 'DronFacade',
      imagenConGamma1:"Usos.png",
      imagenFondo1:"droneFacade2.png",
    }
  },
 
};
</script>
<style>

.container2ie{
    height: 35vh;
    text-align: center;
    vertical-align: middle;
    font-weight: bold;
    padding: 12rem 0rem 0rem 0rem;
}
.fondo1{
    /*background: url(imagen.png) no-repeat center center fixed;*/
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    /*opacity:0.2;*/
}
.inventeye-title{
    color: rgb(221, 225, 236);
    /*color: RGB(27,34,44);*/
    font-size: 320%;
    text-shadow: -0.2px -0.2px  rgb(173, 173, 173), 0.2px -0.2px  rgb(173, 173, 173), -0.2px 0.2px  rgb(173, 173, 173),-0.2px 0.2px  rgb(173, 173, 173); 
    size: 40vh;
    /*background: rgba(0, 0, 0, 0.6);*/
}

</style>
