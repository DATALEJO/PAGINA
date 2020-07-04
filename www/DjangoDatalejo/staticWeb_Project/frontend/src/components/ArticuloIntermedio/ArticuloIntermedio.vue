<template >
  <section :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
    <div class="container-fluid" >
      <div class="row">
        <div class="col-md-12">
          <div class="interbox" >
            <div class="textArticle" align="center"  padding="100px">{{articuloInter}}</div>
          </div>
        </div>
      </div>
    </div>   
  </section>
</template> 

<script>
export default {   
  name: 'articuloIntermedio',
  props: {
      articuloInter:{
        type: String,
        default:"que chevere"
    },
  }
};
</script>
<style scoped>

.interbox{
  margin: 5em;
  font-size: medium;
}
.container-fluid{
  position: relative;
  /*height: 500px;*/
  /*width: 100%;*/
  padding: 0vh;
  padding: 5px 0px 5px 0px;
}

.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  font-size: 16px;

}
</style>
