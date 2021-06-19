<template>
	<div class="section">
        <p class="section__title">Ustawienia</p>
        <div class="link-list">
            <div 
                class="link flex-center"
                :class="{ 'link__current': currentTab === 'user' }"
            >
                <a 
                    href=""
                    @click.prevent="() => setCurrentTab('user')"
                >
                    <p>Użytkownik</p>
                </a>
            </div>
            <div 
                class="link flex-center"
                :class="{ 'link__current': currentTab === 'publisher' }"
            >
                <a 
                    href=""
                    @click.prevent="() => setCurrentTab('publisher')"
                >
                    <p>Sprzedający</p>
                </a>
            </div>
        </div>
    </div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapMutations } = createNamespacedHelpers('ui');


export default {
    computed: mapState(['currentTab']),
    methods: mapMutations(['setCurrentTab'])
}
</script>