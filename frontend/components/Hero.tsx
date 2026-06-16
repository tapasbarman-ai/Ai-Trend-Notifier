import SubscribeForm from './SubscribeForm';

export default function Hero() {
    return (
        <section className="relative overflow-hidden pt-12 pb-20 px-6 md:px-margin-desktop bg-background text-on-background">
            <div className="max-w-container-max-width mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div className="z-10 text-left">
                    <div className="inline-flex items-center gap-2 bg-primary-container/30 text-on-primary-container px-4 py-1.5 rounded-full mb-8">
                        <span className="font-sans text-caption font-bold tracking-wider uppercase text-[11px]">TRUSTED BY 1,500+ PROFESSIONALS</span>
                    </div>
                    
                    <h1 className="font-display text-headline-lg-mobile md:text-display-xl mb-6 text-on-background uppercase">
                        DIVE INTO THE <span className="text-primary-container bg-inverse-surface px-4 inline-block rounded-lg">FUTURE</span> OF AI
                    </h1>
                    
                    <p className="font-sans text-body-lg text-on-surface-variant mb-10 max-w-xl">
                        Professional-grade analysis delivered directly to your inbox. We parse millions of social signals to bring you the insights that actually matter.
                    </p>
                    
                    {/* High-Conversion Subscription Form */}
                    <div className="relative max-w-md" id="subscribe">
                        <SubscribeForm />
                    </div>
                    
                    {/* Hero Trust Metrics */}
                    <div className="mt-12 flex flex-wrap gap-12 pt-8 border-t border-outline-variant">
                        <div>
                            <div className="font-display text-headline-md text-on-background">99%</div>
                            <div className="font-sans text-caption text-on-surface-variant uppercase">Sentiment Accuracy</div>
                        </div>
                        <div className="border-l border-outline-variant pl-12">
                            <div className="font-display text-headline-md text-on-background">2.4ms</div>
                            <div className="font-sans text-caption text-on-surface-variant uppercase">Analysis Speed</div>
                        </div>
                    </div>
                </div>
                
                {/* Visual Accent Container on Right */}
                <div className="relative">
                    <div className="relative z-10 rounded-3xl overflow-hidden border-2 border-primary-container glow-yellow aspect-[4/3] bg-surface-container-low">
                        <img 
                            src="https://lh3.googleusercontent.com/aida-public/AB6AXuD0sbtTDck6X1ioI6XyNEvIUwodXi3L6iXxNXsqqjJhuCsFiREnas_KH7VGGWGbBvZKTsvkReiITXRIiPuKhl96iWVaKzxNf_jQQabFQ8DYULB56IMJAtRyZHv8ZwetEfalJrgxBOkXRBn9xt_VV1hrcMLoT7RpKfH0gLlt2qrRi3vcHTw55aivEyXijYVBbmedc62PAvLRKCacRefjpNHH2IvbgfHYrGzP49Qlw8eSZW-DWodB5lDUc0rfn121dPHwe6PMLqREFqw" 
                            alt="AI Insights Signature Illustration" 
                            className="w-full h-full object-cover"
                        />
                    </div>
                    {/* Decorative radial glows */}
                    <div className="absolute -top-10 -right-10 w-40 h-40 bg-primary-container/20 rounded-full blur-3xl"></div>
                    <div className="absolute -bottom-10 -left-10 w-64 h-64 bg-surface-container-high rounded-full blur-3xl"></div>
                </div>
            </div>
        </section>
    );
}
