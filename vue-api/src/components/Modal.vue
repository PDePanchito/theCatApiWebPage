<template>
<div class="modal fade" id="cat-modal" tabindex="-1" aria-labelledby="cat-modal-label" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="cat-modal-label">{{ selectedCat.name }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img :src="selectedCat.url" alt="Gatito" class="img-fluid rounded">
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  data() {
    return {
      cats: [],
      selectedCat: null
    };
  },
  methods: {
    showCatModal(cat) {
      this.selectedCat = cat;
      $("#cat-modal").modal("show");
    }
  }
}

</script>

<style>
.modal-lg {
    max-width: 100%;
  }
  
  .modal-body .img-fluid {
    width: 100%;
    height: auto;
    max-height: 90vh;
  }
  
</style>