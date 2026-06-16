'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import api from '@/utils/api';
import Link from 'next/link';
import { Mail, Lock, BarChart3, ArrowRight, Eye, EyeOff, HelpCircle, Shield, Activity } from 'lucide-react';

export default function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);
        try {
            const formData = new FormData();
            formData.append('username', email);
            formData.append('password', password);

            const response = await api.post('/auth/token', formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
            });

            localStorage.setItem('token', response.data.access_token);
            router.push('/admin');
        } catch (err) {
            setError('Invalid professional email or access password');
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
            <div className="w-full max-w-[480px] z-10 py-12">
                {/* Brand Identity */}
                <div className="text-center mb-10 space-y-2">
                    <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-primary-container mb-4 shadow-sm border-2 border-primary">
                        <BarChart3 className="text-on-primary-container h-8 w-8" />
                    </div>
                    <h1 className="font-display text-headline-lg text-on-background">
                        AI Insights <span className="text-primary">Admin Portal</span>
                    </h1>
                    <p className="text-on-surface-variant font-sans text-body-md opacity-80">
                        Secure access to the corporate analytics engine
                    </p>
                </div>

                {/* Login Card */}
                <div className="bg-white dark:bg-black border border-outline-variant rounded-xl p-8 md:p-10 shadow-sm relative overflow-hidden">
                    {/* Left Accent Bar */}
                    <div className="absolute left-0 top-0 bottom-0 w-1 bg-primary"></div>
                    
                    <form onSubmit={handleSubmit} className="space-y-6">
                        {/* Email Field */}
                        <div className="space-y-1.5 group">
                            <label className="block font-sans text-label-bold text-on-surface-variant group-focus-within:text-primary transition-colors" htmlFor="email">
                                Professional Email
                            </label>
                            <div className="relative flex items-center border-b border-outline-variant py-3 focus-within:border-primary transition-all">
                                <Mail className="text-outline h-5 w-5 absolute left-0" />
                                <input
                                    id="email"
                                    type="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className="w-full bg-transparent border-none focus:outline-none focus:ring-0 pl-9 pr-2 py-0 text-on-surface font-sans text-body-md placeholder:text-outline/40"
                                    placeholder="admin@ai-insights.com"
                                    required
                                    disabled={loading}
                                />
                            </div>
                        </div>

                        {/* Password Field */}
                        <div className="space-y-1.5 group">
                            <div className="flex justify-between items-end">
                                <label className="block font-sans text-label-bold text-on-surface-variant group-focus-within:text-primary transition-colors" htmlFor="password">
                                    Access Password
                                </label>
                                <a className="text-caption font-sans text-primary hover:underline transition-all" href="#">
                                    Forgot?
                                </a>
                            </div>
                            <div className="relative flex items-center border-b border-outline-variant py-3 focus-within:border-primary transition-all">
                                <Lock className="text-outline h-5 w-5 absolute left-0" />
                                <input
                                    id="password"
                                    type={showPassword ? 'text' : 'password'}
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className="w-full bg-transparent border-none focus:outline-none focus:ring-0 pl-9 pr-10 py-0 text-on-surface font-sans text-body-md placeholder:text-outline/40"
                                    placeholder="••••••••••••"
                                    required
                                    disabled={loading}
                                />
                                <button
                                    type="button"
                                    onClick={() => setShowPassword(!showPassword)}
                                    className="absolute right-0 text-outline hover:text-on-surface-variant transition-colors"
                                >
                                    {showPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                                </button>
                            </div>
                        </div>

                        {error && (
                            <p className="text-rose-600 text-caption font-caption bg-rose-50 border border-rose-100 rounded-lg p-2.5">
                                {error}
                            </p>
                        )}

                        {/* Remember Me Option */}
                        <div className="flex items-center space-x-3 py-2">
                            <input
                                id="remember"
                                type="checkbox"
                                className="w-5 h-5 rounded border-outline text-primary focus:ring-primary transition-all cursor-pointer bg-white"
                            />
                            <label className="text-caption font-sans text-on-surface-variant cursor-pointer select-none" htmlFor="remember">
                                Stay signed in for 30 days
                            </label>
                        </div>

                        {/* Submit Action Button */}
                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full bg-primary-container text-on-primary-container font-sans text-label-bold py-4 rounded-lg border-2 border-primary hover:shadow-lg hover:shadow-primary-container/20 transition-all duration-300 flex items-center justify-center gap-2 group active:scale-95 disabled:opacity-50"
                        >
                            {loading ? 'Verifying access...' : 'Sign In to Portal'}
                            <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1" />
                        </button>
                    </form>

                    {/* Footer text warning */}
                    <div className="mt-8 pt-8 border-t border-outline-variant/30 text-center">
                        <p className="text-caption font-sans text-on-surface-variant leading-relaxed">
                            Authorized personnel only. <br />
                            Activity is monitored and recorded.
                        </p>
                    </div>
                </div>

                {/* Helper info links */}
                <div className="mt-8 flex flex-wrap justify-center gap-x-6 gap-y-2">
                    <Link href="#" className="text-caption font-sans text-on-surface-variant hover:text-primary transition-colors flex items-center gap-1">
                        <HelpCircle className="h-4 w-4" /> Help Center
                    </Link>
                    <Link href="#" className="text-caption font-sans text-on-surface-variant hover:text-primary transition-colors flex items-center gap-1">
                        <Shield className="h-4 w-4" /> Privacy Policy
                    </Link>
                    <Link href="#" className="text-caption font-sans text-on-surface-variant hover:text-primary transition-colors flex items-center gap-1">
                        <Activity className="h-4 w-4" /> System Status
                    </Link>
                </div>
            </div>
        </div>
    );
}
