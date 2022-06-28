<template>
  <div>
    

    <b-button v-b-modal.modal-prevent-closing>
        <b-icon icon="plus" font-scale="1"  ></b-icon>
    </b-button>

    <label class="label">Agregar articulo:</label>

    <div class="mt-3">
      List of articles:
      <b-table striped hover :items="submittedNames" :fields="fields"></b-table>
      
    </div>
    <div v-if="submittedNames.length">  
      <label class="myFile">    
        <b-icon icon="images" class="border rounded p-1" font-scale="3"  ></b-icon>
        <b-form-file class= "file" multiple :file-name-formatter="formatNames" @change="onFileSelected" lang="es"  style="display: none;" > </b-form-file>    
        <label class="custom-file-label" for="customFileLang">Por favor Seleccionar imagenes</label>
      </label>    
    </div>
    

    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Submit Your Name"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Name"
          label-for="name-input"
        > 
          <label class="label">ITEM N°:</label>         
          <b-form-input
            id="itemN-input"
            v-model="itemN"
            required
          ></b-form-input>
          <label class="label">PACKING REFERENCE</label>  
          <b-form-input
            id="packing-input"
            v-model="packing"
            required
          ></b-form-input>
          <label class="label">ARTICLES</label>  
          <b-form-input
            id="description-input"
            v-model="description"
            required
          ></b-form-input>
          <label class="label">CONDITION AT ORIGIN</label>  
          <b-form-input
            id="condition-input"
            v-model="condition"
            required
          ></b-form-input>
          <label class="label">EXCEPTIONS AT DESTINATION</label>  
          <b-form-input
            id="exceptions-input"
            v-model="exceptions"
            required
          ></b-form-input>

          

          Input Value: {{ barcode || "Nothing" }}
          <StreamBarcodeReader
                @decode="onDecode"
                @loaded="onLoaded"
            ></StreamBarcodeReader>

        </b-form-group>
      </form>
    </b-modal>    

  </div>
</template>

<script>
import { StreamBarcodeReader } from "vue-barcode-reader";
import axios from "axios";

  export default {
    components: {
    StreamBarcodeReader,
  },
    data() {
      return {
        nameState: null,        
        itemN: '',
        barcode: '',
        packing: '',
        description: '',
        condition: '',
        exceptions: '',
        submittedNames: [],
        fields: ['item', 'packing', 'articles', 'condition', 'exceptions'],
        selectedFile: null
        
      }
    },
    methods: {

      onFileSelected(event){        

        var token_drop = localStorage.getItem("token_drop");            
        console.log("Get value !!!!!!!!!!!!!!!");
        console.log(token_drop);

        var Dropbox = require('dropbox').Dropbox;
        var dbx = new Dropbox({ accessToken: token_drop.replace(/['"]+/g, '')});
        this.inventory_table = JSON.parse(localStorage.getItem("inventory_table") || '[]')
        axios.post("https://api.dropboxapi.com/2/files/create_folder_v2", {"path": "/" + this.inventory_table['reference'] + "/Empaque","autorename": false}, {
                headers: {
                    'Authorization': `Bearer ${token_drop.replace(/['"]+/g, '')}` 
                    }
          })

        this.selectedFile = event.target.files;

        Array.from(this.selectedFile).forEach(File => { 
          dbx.filesUpload({path: '/'+this.inventory_table['reference'] +'/Empaque/' + File.name, contents: File})
            .then(function(response) {
              console.log(response);
            })
            .catch(function(error) {
              console.error(error);
            });      
          });
      },



      checkFormValidity() {
        const valid = this.$refs.form.checkValidity()
        this.nameState = valid
        return valid
      },
      resetModal() {
        this.nameState= null       
        this.itemN= ''
        this.barcode= ''
        this.packing= ''
        this.description= ''
        this.condition= ''
        this.exceptions= ''
      },
      handleOk(bvModalEvt) {
        // Prevent modal from closing
        bvModalEvt.preventDefault()
        // Trigger submit handler
        this.handleSubmit()
      },
      handleSubmit() {
        // Exit when the form isn't valid
        if (!this.checkFormValidity()) {
          return
        }
        // Push the name to submitted names
        let json = {
          "item":this.itemN, 
          "packing":this.packing,
          "articles":this.description,
          "condition":this.condition,
          "exceptions":this.exceptions,
          "barcode":this.barcode
        }
                   
            
        this.submittedNames.push(json)
        this.$emit('can-continue', {value: true}); 
        localStorage.setItem('inventory_table_detail',JSON.stringify(this.submittedNames));
        // Hide the modal manually
        this.$nextTick(() => {
          this.$bvModal.hide('modal-prevent-closing')
        })
      },
    onDecode (result) {
        this.barcode = result;     
      }
    },
    created: function () {
    const ref = 'https://www.dropbox.com/oauth2/authorize?response_type=code&client_id='+ process.env.VUE_APP_DROPBOX +'&redirect_uri=https://container-grouplii-frontend-uymd3d36pa-uc.a.run.app/auth&token_access_type=offline'
        window.open(ref, "_blank");
    } 
  }
</script>

<style scoped>




.button_add{
    background-color: rgb(255, 255, 255);
}


.custom-file-label {
  white-space: nowrap;
  overflow-x: hidden;
  display: inline-block;
  
}

.myFile {
  position: relative;
  overflow: hidden;
  float: left;
  clear: left;
}
.myFile input[type="file"] {
  display: block;
  position: absolute;
  top: 0;
  right: 0;
  opacity: 0;
  font-size: 100px;
  filter: alpha(opacity=0);
  cursor: pointer;
}
</style>