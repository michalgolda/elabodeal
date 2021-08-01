<template>
    <div class="wrapper">
        <PublisherTypeChooser v-if="!formType" />
        <InvidualPublisherForm v-if="formType" />
    </div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

import PublisherTypeChooser from './PublisherTypeChooser';
import InvidualPublisherForm from './InvidualPublisherForm';


const { mapState: mapUiState  } = createNamespacedHelpers('ui');


export default {
    computed: mapUiState(['formType']),
    components: {
        PublisherTypeChooser,
        InvidualPublisherForm
    }
}
</script>