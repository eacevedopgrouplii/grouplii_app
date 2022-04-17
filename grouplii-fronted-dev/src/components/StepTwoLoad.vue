<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        
        <div class="field">
            <label class="label">NOMBRE DEL CLIENTE:</label>
            <div class="control">
                {{form.clientName}}
                
            </div>
        </div>
        <div class="field">
            <label class="label">REFERENCIA:</label>
            <div class="control">
                {{form.reference}}
                
            </div>
        </div>
        <div class="field">
            <label class="label">FECHA:</label>
            <div class="control">
                {{form.date}}
            </div>
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
                    clientName: '',
                    reference: '',
                    date: ''
                }
            }
        },
        validations: {
            form: {
                clientName: {
                    required
                },
                reference: {
                    required
                },
                date: {
                    required
                }
            }
        },
        watch: {
            $v: {
                handler: function (val) {
                    if(!val.$invalid) {
                        this.$emit('can-continue', {value: true});
                        localStorage.setItem('load_unload_table',JSON.stringify({...this.form_total,...this.form}));
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
                    const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();                                                         
                    this.form.date = date;
                }
        },

        created(){
            this.data_inventory = JSON.parse(localStorage.getItem("inventory_reference") || '[]');
            this.form.reference = this.data_inventory[0];
            this.form.clientName = this.data_inventory[1];
            this.getNow();
            this.form_total = JSON.parse(localStorage.getItem("load_unload_table") || '[]');
        }
    }
</script>

