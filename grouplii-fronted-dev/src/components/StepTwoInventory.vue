<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <div class="field">
            <label class="label">DESTINATION:</label>
            <div class="control">
                <input :class="['input', ($v.form.via.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.destination">
            </div>
        </div>      
                <div class="col-sm-3">             
            <label class="label">VIA:</label>
            <select :class="['input', ($v.form.destination.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.via">>
                <option value="AIR">AIR</option>
                <option value="SEA">SEA</option>
                <option value="TRUCK">TRUCK</option>
            </select>
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
                    via: '',
                    destination: ''
                },
                form_total : []
            }
        },
        validations: {
            form: {
                via: {
                    required
                },
                destination: {
                    required
                }
            }
        },
        watch: {
            $v: {
                handler: function (val) {
                    if(!val.$invalid) {
                        this.$emit('can-continue', {value: true}); 
                        localStorage.setItem('inventory_table',JSON.stringify({...this.form_total,...this.form}));

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
            this.form_total = JSON.parse(localStorage.getItem("inventory_table") || '[]');

            if(!this.$v.$invalid) {
                this.$emit('can-continue', {value: true});
            } else {
                this.$emit('can-continue', {value: false});
            }
        }
    }
</script>