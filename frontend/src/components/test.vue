<template>
  <div>
    <div id="app">
      <full-page :options="options" id="fullpage" ref="fullpage">
        <div class="section">
          <h3>그것이 무엇이든 다~ 있다!</h3>
        </div>
        <div class="section">
          <h3>Section 3</h3>
        </div>
      </full-page>
    </div>
  </div>
</template>

<script>
import http from "../services/http-common.js";

export default {
  data() {
    return {
      options: {
        afterLoad: this.afterLoad,
        navigation: true,
        anchors: ["page1", "page3"],
        sectionsColor: [
          "#41b883",
          "#ff5f45",
          "#0798ec",
          "#fec401",
          "#1bcee6",
          "#ee1a59",
          "#2c3e4f",
          "#ba5be9",
          "#b4b8ab"
        ]
      }
    };
  },
  methods: {
    afterLoad: function(origin, destination, direction) {
      console.log("After load....");
      console.log(destination);
    },
    addSection: function(e) {
      var newSectionNumber =
        document.querySelectorAll(".fp-section").length + 1;

      // creating the section div
      var section = document.createElement("div");
      section.className = "section";
      section.innerHTML = `<h3>Section ${newSectionNumber}</h3>`;

      // adding section
      document.querySelector("#fullpage").appendChild(section);

      var sectionMenuItem = document.createElement("li");
      sectionMenuItem.setAttribute(
        "data-menuanchor",
        "page" + newSectionNumber
      );
      sectionMenuItem.innerHTML = `<a href="#page${newSectionNumber}">Section${newSectionNumber}</a>`;

      this.options.anchors.push(`page${newSectionNumber}`);

      this.$refs.fullpage.build();
    },

    removeSection: function() {
      var sections = document
        .querySelector("#fullpage")
        .querySelectorAll(".fp-section");
      var lastSection = sections[sections.length - 1];

      // removing the last section
      lastSection.parentNode.removeChild(lastSection);

      // removing the last anchor
      this.options.anchors.pop();

      // removing the last item on the sections menu
      var sectionsMenuItems = document.querySelectorAll("#menu li");
      var lastItem = sectionsMenuItems[sectionsMenuItems.length - 1];
      lastItem.parentNode.removeChild(lastItem);
    }
  },

  beforeMount() {
    // this.test();
  }
};
</script>

<style>
a {
  text-decoration: none;
}
table {
  border-spacing: 0;
}
fieldset,
img {
  border: 0;
}
address,
caption,
cite,
code,
dfn,
em,
strong,
th,
var {
  font-weight: normal;
  font-style: normal;
}
strong {
  font-weight: bold;
}
caption,
th {
  text-align: left;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: normal;
  font-size: 100%;
  margin: 0;
  padding: 0;
}
q:before,
q:after {
  content: "";
}
abbr,
acronym {
  border: 0;
}
* {
  -webkit-box-sizing: border-box; /* Safari<=5 Android<=3 */
  -moz-box-sizing: border-box; /* <=28 */
  box-sizing: border-box;
}

/* Custom
 * --------------------------------------- */
body {
  font-family: arial, helvetica;
}
.section {
  position: relative;
  text-align: center;
}
#section-1 h2 {
  color: #fff;
  font-size: 10em;
  font-weight: 900;
}
#section-1 h1 {
  font-size: 2em;
  font-weight: 100;
  -webkit-font-smoothing: antialiased;
  -moz-font-smoothing: antialiased;
  margin: 1.5em auto 1em auto;
  color: #35495e;
  padding-right: 30px;
  padding-left: 30px;
}
#section-1 li {
  display: inline-block;
  margin: 1.25em 0.3em;
}
.section-1-button {
  padding: 0.93em 1.87em;
  background: #35495e;
  border-radius: 5px;
  display: block;
  color: #fff;
}
h3 {
  font-size: 2em;
  margin-bottom: 500px;
  text-align: center;
  color: #fff;
  font-weight: bold;
}
#logo {
  position: fixed;
  top: 20px;
  left: 20px;
  color: #fff;
  font-weight: bold;
  z-index: 99;
  font-size: 1.9em;
  -webkit-font-smoothing: antialiased;
  -moz-font-smoothing: antialiased;
}

/* Menu
 * --------------------------------------- */
#menu-line {
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 159px;
  height: 2px;
  background: #fff;
}

#menu {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 70;
  -webkit-font-smoothing: antialiased;
  -moz-font-smoothing: antialiased;
  letter-spacing: 1px;
  font-size: 1.1em;
}
#menu li {
  display: inline-block;
  margin: 10px 0px;
  position: relative;
}
#menu a {
  color: #fff;
  padding: 0 1.1em 1.1em 1.1em;
}
#menu li.active a:after {
  content: "";
  margin: 0 1.1em 0 1.1em;
  height: 2px;
  background: #fff;
  display: block;
  position: absolute;
  bottom: -6px;
  left: 0;
  right: 0;
  display: block;
}

/* Actions buttons
 * --------------------------------------- */
.actions {
  position: fixed;
  bottom: 2%;
  margin: 0 auto;
  z-index: 99;
  left: 0;
  right: 0;
  text-align: center;
}
.actions li {
  display: inline-block;
  margin: 0.3em 0.3em;
}
.actions-button {
  padding: 0.73em 1.47em;
  background: rgba(53, 73, 94, 0.47);
  border-radius: 5px;
  display: block;
  color: #fff;
  cursor: pointer;
}
</style>
