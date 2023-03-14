<!-- Component that adds a button to scroll back to the top of the page in a smooth way. Not looking the way i would like yet. -->

<template>
    <div class="scroll-top">
      <button class="btn btn-primary me-md-2" @click="scrollToTop">
        <h1 class="message">&#8593;	</h1>
      </button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      scrollToTop() {
        window.scrollTo({
          top: 0,
          behavior: "smooth",
        });
      },
    },
  };
  </script>
  
  <style>
 
  .btn {
    filter: opacity(0.6);
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 999;  
    border-radius: 100%;
  }
  
  .scroll-top i {
    transform: rotate(-90deg);
  }
  </style>
  