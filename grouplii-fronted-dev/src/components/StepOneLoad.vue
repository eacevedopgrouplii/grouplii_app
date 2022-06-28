<template>
    <div style="padding: 2rem 3rem; text-align: left; margin-top: 5%;">
        <div class="col-sm-3">             
            <label class="label">TIPO DE CONTENEDOR: </label>
            <select :class="['input', ($v.form.container.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.container">>
                <option value="20">20</option>
                <option value="40">40</option>
                <option value="HC">HC</option>
            </select>
        </div>
        
        <div class="field">
            <label class="label">NÚMERO DE CONTENEDOR: </label>
            <div class="control">
                <input :class="['input', ($v.form.containerNumber.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.containerNumber">
            </div>
        </div>
        <div class="field">
            <label class="label">TARA:</label>
            <div class="control">
                <input :class="['input', ($v.form.tare.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.tare">
            </div>
        </div>
        <div class="field">
            <label class="label">HORA DE INICIO:</label>
            <div class="control">
                {{form.hourStart}}
            </div>
        </div>
        <div class="field">
            <label class="label">ESPACIO SOBRANTE: </label>
            <div class="control">
                <input :class="['input', ($v.form.space.$error) ? 'is-danger' : '']"  type="text" placeholder="Email input" v-model="form.space">
            </div>            
        </div>   
        <div class="field">
            <label class="label">FOTOS:</label>
            <div class="control">
                <input :class="['input', ($v.form.photosNumber.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.photosNumber">
            </div>
        </div>    
        <div class="field">
            <label class="label">EMAIL_SEND:</label>
            <div class="control">
                <input :class="['input', ($v.form.email_send.$error) ? 'is-danger' : '']"  type="text" placeholder="Email to send input" v-model="form.email_send">
            </div>
            <p v-if="$v.form.email_send.$error" class="help is-danger">This email is invalid</p>
        </div>  
    </div>
</template>

<script>
import {validationMixin} from 'vuelidate'
import {required} from 'vuelidate/lib/validators'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                form: {                    
                    container: '',
                    containerNumber: '',
                    tare: '',
                    hourStart: '',                    
                    space: '',
                    photosNumber: '',
                    email_send: ''
                }
            }
        },
        validations: {
            form: {
                container: {
                    required
                },
                containerNumber: {
                    required
                },
                tare: {
                    required
                },
                hourStart: {
                },
                space: {
                    required               
                },
                photosNumber:{
                    required
                },
                email_send:{

                }
            }
        },
        watch: {
            $v: {
                handler: function (val) {
                    if(!val.$invalid) {
                        this.$emit('can-continue', {value: true});
                        localStorage.setItem('load_unload_table',JSON.stringify(this.form));
                    } else {
                        this.$emit('can-continue', {value: false});
                    }
                },
                deep: true
            },
            clickedNext(val) {
                if(val === true) {
                    this.$v.form.$touch();
                }
            }
        },
        mounted() {
            if(!this.$v.$invalid) {
                this.$emit('can-continue', {value: true});                
            } else {
                this.$emit('can-continue', {value: false});
            }
            
        },

        methods: {
                getNow: function() {
                    const today = new Date();                    
                    const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();                    
                    this.form.hourStart = time;
                }
        },

        created() {
                this.getNow();
        }
    }
</script>