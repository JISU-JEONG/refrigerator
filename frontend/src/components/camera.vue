<template>
  <div class="img">
    <div v-if="!image">
      <h2>Select an image</h2>
      <input type="file" @change="onFileChange" />
    </div>
    <div v-else>
      <img :src="image" />
      <button @click="removeImage">Remove image</button>
    </div>
    <br />
    <input type="checkbox" id="one" value="One" v-model="picked" />
    <label for="one">One</label>
    <br />
    <input type="checkbox" id="two" value="Two" v-model="picked" />
    <label for="two">Two</label>
    <br />
    <span>선택: {{ picked }}</span>
  </div>
</template>

<script>
export default {
  name: "camera",
  components: {},
  data: () => ({
    image: "",
    picked: []
  }),
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;

      reader.onload = e => {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function(e) {
      this.image = "";
    }
  }
};
</script>

<style scoped>
.img {
  width: 100%;
  height: 100vh;
  padding-top: 80px;

  text-align: center;
}
img {
  width: 30%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
</style>
