<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <b-row>
            <b-col>
                <div class="field">
                    <label class="label">TOTAL PIEZAS:</label>
                    <div class="control">
                        <input :class="['input', ($v.form.totalPieces.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                            v-model="form.totalPieces">
                    </div>
                </div> 
            </b-col>    
            <b-col>
                <div class="field">
                    <label class="label">TOTAL VANES:</label>
                    <div class="control">
                        <input :class="['input', ($v.form.totalVans.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                            v-model="form.totalVans">
                    </div>
                </div>
            </b-col>
            <b-col>
            <div class="field">
                <label class="label">VOLUMEN M3:</label>
                <div class="control">
                    <input :class="['input', ($v.form.volumeM3.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                        v-model="form.volumeM3">
                </div>
            </div> 
        </b-col>
        </b-row>

        <div class="field">
            <label class="label">RECIBIDO POR:</label>
            <div class="control">
                <input :class="['input', ($v.form.received.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.received">
            </div>
        </div>
        <div class="field">
            <label class="label">ENTREGADO POR:</label>
            <div class="control">
                <input :class="['input', ($v.form.delivered.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.delivered">
            </div>
        </div>
        <b-row>
            <b-col>
                <div class="field">
                    <label class="label">PERSONAL INVOLUCRADO:</label>
                    <div class="control">
                        <input :class="['input', ($v.form.personnel.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                            v-model="form.personnel">
                    </div>
                </div>
            </b-col>
            <b-col>
                <div class="col-sm-3">             
                    <label class="label">EMPAQUE/DESEMPAQUE: </label>
                    <select :class="['input', ($v.form.packing.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                            v-model="form.packing">>
                        <option value="packing">EMPAQUE</option>
                        <option value="unpacking">DESEMPAQUE</option>
                    </select>
                </div>
             </b-col>
        </b-row>
        <b-row>
            <b-col>
                <div class="field">
                    <label class="label">PERSONAL INVOLUCRADO:</label>
                    <div class="control">
                        <input :class="['input', ($v.form.personnel1.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                            v-model="form.personnel1">
                    </div>
                </div>
            </b-col>
            <b-col>
                <div class="col-sm-3">             
                    <label class="label">CARGUE/DESCARGUE: </label>
                    <select :class="['input', ($v.form.load.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                            v-model="form.load">>
                        <option value="load">CARGUE</option>
                        <option value="unload">DESCARGUE</option>
                    </select>
                </div>
            </b-col>
        </b-row>
        <div class="field">
            <label class="label">PRECINTOS UTILIZADOS:</label>
            <div class="control">
                <input :class="['input', ($v.form.seals.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.seals">
            </div>
        </div>
        <div class="field">
            <label class="label">PLACA VEHICULO:</label>
            <div class="control">
                <input :class="['input', ($v.form.licensePlate.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.licensePlate">
            </div>
        </div>
        <div class="field">
            <label class="label">CONSOLIDADO:</label>
            <div class="control">
                <input :class="['input', ($v.form.consolidated.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.consolidated">
            </div>
        </div>
        <div class="field">
            <label class="label">OBSERVACIONES:</label>
            <div class="control">
                <input :class="['input', ($v.form.observations.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.observations">
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
                    totalPieces: '',
                    totalVans: '',
                    volumeM3: '',
                    received: '',
                    delivered: '',
                    personnel: '',
                    packing: '',
                    personnel1: '',
                    load: '',
                    seals: '',
                    licensePlate: '',
                    consolidated: '',
                    observations: ''                                         
                }
            }
        },
        validations: {
            form: {
                totalPieces: {
                    required
                },
                totalVans: {
                    required
                },
                volumeM3: {
                    required
                },
                received: {
                    required
                },
                delivered: {
                    required
                },
                personnel: {
                    required
                },
                packing: {
                    required
                },
                personnel1: {
                    required
                },
                load: {
                    required
                },
                seals: {
                    required
                },
                licensePlate: {
                    required
                },
                consolidated: {
                    required
                },
                observations: {
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
        created() {
            this.form_total = JSON.parse(localStorage.getItem("load_unload_table") || '[]');
        }
    }
</script>