<!-- Component that renders a title for every page -->

<template>
  <div class="text-center">
    <nav class="navbar navbar-expand-lg navbar-dark d-none d-lg-block" style="z-index: 2000;">
        <div class="container-fluid">
          <a class="navbar-brand nav-link" target="_blank" href="https://www.youtube.com/watch?v=_9ZKOLVEjJI&ab_channel=GatosGraciosos">
            <strong>Galería de gatitos</strong>
          </a>
          <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#navbarExample01"
            aria-controls="navbarExample01" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fas fa-bars"></i>
          </button>
          <div class="collapse navbar-collapse" id="navbarExample01">
          </div>
        </div>
      </nav>
    </div>
</template>

<!-- This exports the component and allows us to use it outside this file  -->

<script>
export default {
    name: "Header",
   
}
</script>

<style>
.navbar .nav-link {
    color: #fff !important;
  }
  
</style>