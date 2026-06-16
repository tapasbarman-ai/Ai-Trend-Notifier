'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import api from '@/utils/api';
import Link from 'next/link';
import { Mail, Lock, User, ArrowRight, ShieldCheck, Database, Cloud, History, Sparkles, LayoutGrid } from 'lucide-react';

export default function RegisterPage() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [focus, setFocus] = useState('analytics');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);
        try {
            await api.post('/auth/register', { email, password });
            router.push('/login');
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Registration failed. Please contact your administrator.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div 
            className="min-h-screen flex flex-col justify-center items-center px-margin-mobile relative text-on-background bg-[#f9f9ff]"
            style={{
                backgroundImage: 'radial-gradient(#dce2f3 0.5px, transparent 0.5px)',
                backgroundSize: '24px 24px'
            }}
        >
            <div className="w-full max-w-xl z-10 py-12">
                {/* Registration Card */}
                <div className="bg-white dark:bg-black border border-outline-variant rounded-xl overflow-hidden shadow-sm transition-all duration-300">
                    <div className="p-8 md:p-12 space-y-8">
                        {/* Header */}
                        <div className="text-center">
                            <h1 className="font-display text-3xl font-extrabold text-on-background mb-2">
                                Create Admin Account
                            </h1>
                            <p className="text-on-surface-variant font-sans text-body-md font-semibold opacity-85">
                                Join the AI Insights management team.
                            </p>
                        </div>

                        {/* Form */}
                        <form onSubmit={handleSubmit} className="space-y-6">
                            {/* Full Name */}
                            <div className="group">
                                <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-all">
                                    Full Name
                                </label>
                                <div className="relative flex items-center border-b border-outline-variant py-3 focus-within:border-primary transition-all">
                                    <User className="text-outline h-5 w-5 absolute left-0" />
                                    <input
                                        type="text"
                                        value={name}
                                        onChange={(e) => setName(e.target.value)}
                                        className="w-full bg-transparent border-none focus:outline-none focus:ring-0 pl-9 pr-2 py-0 text-on-surface font-sans text-body-md placeholder:text-outline/40"
                                        placeholder="Alex Rivera"
                                        disabled={loading}
                                    />
                                </div>
                            </div>

                            {/* Email Address */}
                            <div className="group">
                                <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-all">
                                    Email Address
                                </label>
                                <div className="relative flex items-center border-b border-outline-variant py-3 focus-within:border-primary transition-all">
                                    <Mail className="text-outline h-5 w-5 absolute left-0" />
                                    <input
                                        type="email"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        className="w-full bg-transparent border-none focus:outline-none focus:ring-0 pl-9 pr-2 py-0 text-on-surface font-sans text-body-md placeholder:text-outline/40"
                                        placeholder="alex@ai-insights.com"
                                        required
                                        disabled={loading}
                                    />
                                </div>
                            </div>

                            {/* Password */}
                            <div className="group">
                                <label className="block font-sans text-label-bold font-bold text-on-surface-variant mb-1 group-focus-within:text-primary transition-all">
                                    Password
                                </label>
                                <div className="relative flex items-center border-b border-outline-variant py-3 focus-within:border-primary transition-all">
                                    <Lock className="text-outline h-5 w-5 absolute left-0" />
                                    <input
                                        type="password"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                        className="w-full bg-transparent border-none focus:outline-none focus:ring-0 pl-9 pr-2 py-0 text-on-surface font-sans text-body-md placeholder:text-outline/40"
                                        placeholder="••••••••"
                                        required
                                        disabled={loading}
                                    />
                                </div>
                            </div>

                            {/* Focus Radio Grid Selector */}
                            <div className="space-y-3">
                                <label className="block font-sans text-label-bold font-bold text-on-surface-variant">
                                    Primary Focus
                                </label>
                                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                                    {/* Analytics */}
                                    <label className="cursor-pointer">
                                        <input
                                            type="radio"
                                            name="focus"
                                            value="analytics"
                                            checked={focus === 'analytics'}
                                            onChange={() => setFocus('analytics')}
                                            className="hidden peer"
                                        />
                                        <div className="flex flex-col items-center justify-center p-4 border border-outline-variant rounded-lg bg-surface-container-low transition-all hover:bg-surface-container-high peer-checked:border-primary peer-checked:bg-primary-container/10 peer-checked:shadow-sm text-center">
                                            <Database className="h-5 w-5 text-primary mb-2" />
                                            <span className="font-sans text-label-bold font-bold text-on-surface text-xs">Analytics</span>
                                        </div>
                                    </label>
                                    {/* Curation */}
                                    <label className="cursor-pointer">
                                        <input
                                            type="radio"
                                            name="focus"
                                            value="curation"
                                            checked={focus === 'curation'}
                                            onChange={() => setFocus('curation')}
                                            className="hidden peer"
                                        />
                                        <div className="flex flex-col items-center justify-center p-4 border border-outline-variant rounded-lg bg-surface-container-low transition-all hover:bg-surface-container-high peer-checked:border-primary peer-checked:bg-primary-container/10 peer-checked:shadow-sm text-center">
                                            <Sparkles className="h-5 w-5 text-primary mb-2" />
                                            <span className="font-sans text-label-bold font-bold text-on-surface text-xs">Curation</span>
                                        </div>
                                    </label>
                                    {/* Strategy */}
                                    <label className="cursor-pointer">
                                        <input
                                            type="radio"
                                            name="focus"
                                            value="strategy"
                                            checked={focus === 'strategy'}
                                            onChange={() => setFocus('strategy')}
                                            className="hidden peer"
                                        />
                                        <div className="flex flex-col items-center justify-center p-4 border border-outline-variant rounded-lg bg-surface-container-low transition-all hover:bg-surface-container-high peer-checked:border-primary peer-checked:bg-primary-container/10 peer-checked:shadow-sm text-center">
                                            <LayoutGrid className="h-5 w-5 text-primary mb-2" />
                                            <span className="font-sans text-label-bold font-bold text-on-surface text-xs">Strategy</span>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            {error && (
                                <p className="text-rose-600 text-xs font-semibold bg-rose-50 border border-rose-100 rounded-lg p-2.5">
                                    {error}
                                </p>
                            )}

                            {/* Submit Button */}
                            <div className="pt-4">
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className="w-full bg-primary-container text-on-primary-container font-sans text-label-bold font-bold py-4 rounded-xl border-2 border-primary hover:shadow-lg hover:shadow-primary-container/20 transition-all duration-300 flex items-center justify-center gap-2 group active:scale-95 disabled:opacity-50"
                                >
                                    {loading ? 'Creating account...' : 'Create Account'}
                                    <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
                                </button>
                            </div>
                        </form>

                        {/* Footer Link */}
                        <div className="mt-8 text-center pt-4 border-t border-outline-variant/30">
                            <p className="font-sans text-caption font-semibold text-on-surface-variant">
                                Already have an admin account?{' '}
                                <Link className="text-primary font-sans text-label-bold font-bold hover:underline" href="/login">
                                    Log in instead
                                </Link>
                            </p>
                        </div>
                    </div>
                    {/* Decorative Accent Bar */}
                    <div className="h-2 w-full bg-gradient-to-r from-primary-container via-primary-fixed to-primary-container"></div>
                </div>

                {/* Trust Badges */}
                <div className="mt-12 grid grid-cols-2 md:grid-cols-4 gap-4 opacity-70">
                    <div className="flex items-center gap-2 justify-center text-on-surface-variant">
                        <ShieldCheck className="h-4 w-4" />
                        <span className="font-sans text-caption font-bold">Secure SSO</span>
                    </div>
                    <div className="flex items-center gap-2 justify-center text-on-surface-variant">
                        <Lock className="h-4 w-4" />
                        <span className="font-sans text-caption font-bold">256-bit AES</span>
                    </div>
                    <div className="flex items-center gap-2 justify-center text-on-surface-variant">
                        <Cloud className="h-4 w-4" />
                        <span className="font-sans text-caption font-bold">Cloud Sync</span>
                    </div>
                    <div className="flex items-center gap-2 justify-center text-on-surface-variant">
                        <History className="h-4 w-4" />
                        <span className="font-sans text-caption font-bold">Audit Ready</span>
                    </div>
                </div>
            </div>
        </div>
    );
}
