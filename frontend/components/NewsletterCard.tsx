import Link from 'next/link';

interface NewsletterProps {
    id: number;
    title: string;
    summary: string;
    sentiment: string;
    published_at: string;
}

const ILLUSTRATIONS = [
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDp8KRM3FRqabdPr5LIC8nHN3tLVfMp9M-1FW6bU5frPvLgSyX1b97toZI5MDRRC0iQflHFCGltV8PVYceeoql-abOK04w3TlLaauBi9ILwDyUgzVikP9h17jz1pRCu1YJZ0R6Iq_6F2yLZuzgzQinj9w91mw8bUGJnLdzSKI6EIE9OkS6GxNAcS8dfmHC72q0LlyNn8Mta1-6rwxAm4E7Hl84i9HAiuMvf2XPssNFfjOjPgTdNQD1LCQBB0BqUryHYMlAgnYsr1pA',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDTzCqBtzCp6belRx0yLYZHehd09YqA3bzEYv1wkCkDX3toulqfZFcmYvA0um4yiFZ8l1oRah9xRtdIgzRHVxdioylGEldHgRYq6kEh0c1hgi0of7DpVYV_iYnC2293_QrsqI0zaTu8p7b7HmU8bHiB5pwhFrjLRA_DGrpbQb1op7jCm7IoOKctkZEszqy0UzHr3l11pFZq-3wgLbhLeXkwBI0uxthhXcJkrMbLkXPvspeiWztT9GcdRySm353BcRK2Wm9oj5tGh7w',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuAuJazqaZmF6b4chvUO0cEIxSQSx88Vg1bW8bhlI3jqHguXTeX2Pu9Ey0hJ7QQ0ydTDbx5m_i11K4exDu2OJJkqZMX-wNZ00ysNcld4U78HBiTCKHD88FkKP6SMccOiD0rv4DFwJcKVoB_ilSW11pJsYy5gTNRO4DixSa6q9dI8rdcAYvWwHqQihOkxUJQsONARo7H1VPqtFH6P6_T-CRJPmTlRBmQ433b6oqtp0z5Ts6Rwp_h0qU3zHkoYyOgF64_UF1FfvGmuFjE',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDTDf2SoQP58TU8XmXZ1RIH-EnpWHyh6bf-KTcqqNxyxQ18DGE947YP2cK4BbN3xY3RxkAjhLKcBTovjCO2EB1e71se_At2EXDCk6vGVw0ItHSlhFuStizNUP-A81xmpfBQPwrP8wiDGgFPnESeagBfMYVSzkTuXfwNdbOPDCqvlFAMSqv5VAZZ57jvvdvDIMmUoaPvf222HcYh8flr9XDxsIfGcWS9BYFC1RQL5fHByMJdcb86n7S2_PC05_AM3_OyOMGKnsg1-Xs',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDCpJb0FUYCaoqYln3m3bWwIGl-EGA2WgQsTvFR2hSxMJBmOsc_lrTTfPiSWtoQLy35Sy76nTtQE27rjsdH9ehRYabGkCKQGlkTbsPKoif1ZlT1hKs-jz7rppVj4UH4b2Ey7vRec_IEG6DX7BFm7XglwP4H30Juu5yBBx22IPmJOVWILnDXpWjftaSuX9xBNuRV9P4ynY-S8ZWMxPc_ij2s__Q1JvVO6Ki7wx8y8r4K0xp_2izIm2hxG70g3boTm_Z9fhwtWSFHn4k',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuDPNnV3bQPgVLfLzllU2YndPnuXpc79X6mZoKqiMNp-IAXec3Kh56UeglFuAIb_mQd4Dx3mzpMbNY3fvIntHnAWNEQoDGvZUztPut7LiDwbw-EbF9eXGaOLxynhSApyNBpvLOLQ13WbGXxltw87sKuN3ofCHfu_CsW4wEIw-MNWBNwKSVBbZ58HCoEAKZOy9vYW6BztVbT0P44GVHV1pwdTl8SrtmIVyBATq_hU6iPlF8VFbVPjbWJR3qykhI9nGQsoLTkOAHGRIls'
];

export default function NewsletterCard({ id, title, summary, sentiment, published_at }: NewsletterProps) {
    const date = new Date(published_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });

    const getIllustration = () => {
        const text = title.toLowerCase();
        if (text.includes('generative') || text.includes('efficiency') || text.includes('swarm') || text.includes('agent')) {
            return ILLUSTRATIONS[0];
        }
        if (text.includes('robot') || text.includes('haptic') || text.includes('tactile')) {
            return ILLUSTRATIONS[1];
        }
        if (text.includes('distributed') || text.includes('networks') || text.includes('planetary') || text.includes('data')) {
            return ILLUSTRATIONS[2];
        }
        if (text.includes('ethics') || text.includes('transparency') || text.includes('bias') || text.includes('dataset') || text.includes('crisis')) {
            return ILLUSTRATIONS[3];
        }
        if (text.includes('quantum') || text.includes('chip') || text.includes('semiconductor') || text.includes('hardware')) {
            return ILLUSTRATIONS[5];
        }
        if (text.includes('hologram') || text.includes('design') || text.includes('architecture') || text.includes('urban') || text.includes('planning')) {
            return ILLUSTRATIONS[4];
        }
        // Fallback by ID
        return ILLUSTRATIONS[id % ILLUSTRATIONS.length];
    };

    return (
        <article className="group bg-surface-container-lowest border border-outline-variant rounded-2xl overflow-hidden hover:-translate-y-2 hover:shadow-xl transition-all duration-300 flex flex-col justify-between h-full">
            <div>
                {/* Illustrative Pattern Card Header */}
                <div className="aspect-video relative overflow-hidden border-b border-outline-variant bg-surface-container-low">
                    <img 
                        src={getIllustration()} 
                        alt="Edition Context Illustration" 
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                    />
                    <div className="absolute top-4 left-4">
                        <span className={`px-3 py-1 rounded-full text-caption font-caption shadow-sm ${
                            sentiment === 'Positive' ? 'sentiment-gradient-positive text-on-primary-fixed' :
                            sentiment === 'Negative' ? 'bg-error-container text-on-error-container border border-error/20' :
                            'bg-surface-container-highest text-on-surface-variant border border-outline-variant'
                        }`}>
                            {sentiment}
                        </span>
                    </div>
                </div>

                <div className="p-6 pb-0">
                    <p className="font-caption text-caption text-on-surface-variant mb-2">{date}</p>
                    <h3 className="font-headline-md text-headline-md text-on-background mb-4 group-hover:text-primary transition-colors leading-snug">
                        {title}
                    </h3>
                    
                    <div className="summary-accent p-4 mb-6 rounded-r-lg">
                        <p className="font-body-md text-body-md italic text-on-surface line-clamp-3">
                            "{summary}"
                        </p>
                    </div>
                </div>
            </div>

            <div className="px-6 pb-6">
                <Link href={`/newsletters/${id}`} className="flex items-center gap-2 font-label-bold text-label-bold text-primary group/link hover:opacity-80 transition-all w-fit">
                    Read Full Edition 
                    <span className="transition-transform duration-300 group-hover/link:translate-x-1">→</span>
                </Link>
            </div>
        </article>
    );
}
