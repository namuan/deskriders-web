+++
draft = false
date = 2025-11-24T21:11:42Z
title = "DataDog RUM Integration for Website Monitoring: A Complete Guide"
description = "Learn how to implement DataDog Real User Monitoring (RUM) for comprehensive website monitoring, including setup, configuration, dashboard creation, and best practices."
slug = "datadog-rum-website-monitoring"
tags = ["datadog", "rum", "monitoring", "performance", "website", "frontend"]
categories = ["development", "monitoring", "performance"]
externalLink = ""
series = []
+++

**Generated using LLM for reference purposes. Not reviewed and tested and may contain errors.**

# DataDog RUM Integration for Website Monitoring: A Complete Guide

DataDog Real User Monitoring (RUM) provides comprehensive insights into your website's performance and user experience by collecting real-time data from actual user interactions. This guide covers everything you need to know about implementing DataDog RUM for effective website monitoring.

## Table of Contents

1. [DataDog RUM Overview](#datadog-rum-overview)
2. [DataDog RUM Setup & Configuration](#datadog-rum-setup--configuration)
3. [Website Monitoring with DataDog RUM](#website-monitoring-with-datadog-rum)
4. [DataDog Dashboard Creation](#datadog-dashboard-creation)
5. [Implementation Examples](#implementation-examples)
6. [Best Practices](#best-practices)

## DataDog RUM Overview

### What is DataDog RUM?

DataDog Real User Monitoring (RUM) is a powerful tool that automatically collects performance and usage data from real user sessions on your website. It provides deep insights into:

- **Page Load Performance**: Core Web Vitals, page load times, and resource loading
- **User Interactions**: Clicks, navigation patterns, and user flows
- **Error Tracking**: JavaScript errors, API failures, and resource loading issues
- **API Performance**: End-to-end API monitoring and response times
- **User Sessions**: Session replay and user behavior analytics

### Benefits of DataDog RUM vs Custom Solutions

**Advantages of DataDog RUM:**

1. **Zero Configuration Setup**: Automatic collection of Core Web Vitals and performance metrics
2. **Advanced Analytics**: Built-in correlation between frontend performance and backend services
3. **Scalability**: Handles high-volume traffic without infrastructure management
4. **Integration Ecosystem**: Seamless integration with APM, Infrastructure Monitoring, and Log Management
5. **Advanced Features**: Session replay, synthetic monitoring, and anomaly detection
6. **Professional Support**: 24/7 support and regular feature updates

**Compared to Custom Solutions:**
- No need to build and maintain custom monitoring infrastructure
- Reduced development time and ongoing maintenance costs
- Access to advanced ML-powered anomaly detection
- Built-in alerting and dashboard capabilities
- Professional-grade security and compliance

### Key Metrics Available in DataDog RUM

DataDog RUM automatically collects and provides insights into:

#### Core Web Vitals
- **Largest Contentful Paint (LCP)**: Page loading performance
- **First Input Delay (FID)**: Page interactivity
- **Cumulative Layout Shift (CLS)**: Visual stability

#### Performance Metrics
- **Page Load Time**: Total time to load and render pages
- **Resource Loading**: Individual resource performance (JS, CSS, images)
- **API Response Times**: End-to-end API performance
- **DNS and Network Timing**: Network-level performance metrics

#### User Experience Metrics
- **Session Duration**: User engagement and session length
- **Page Views**: Traffic patterns and popular pages
- **User Flows**: Navigation patterns and conversion funnels
- **Error Rates**: JavaScript errors and failed requests

#### Business Metrics
- **Conversion Tracking**: Custom business event monitoring
- **Feature Usage**: User interaction with specific features
- **Geographic Performance**: Performance by user location

## DataDog RUM Setup & Configuration

### DataDog Browser SDK Installation and Setup

#### Step 1: Install DataDog Browser SDK

**Option A: NPM Installation**
```bash
npm install @datadog/browser-rum @datadog/browser-core
```

**Option B: CDN Installation**
```html
<script src="https://www.datadoghq-browser-agent.com/datadog-rum.js"></script>
```

#### Step 2: Initialize DataDog RUM

**Basic Initialization:**
```javascript
import { datadogRum } from '@datadog/browser-rum';

datadogRum.init({
    applicationId: 'YOUR_APPLICATION_ID',
    clientToken: 'YOUR_CLIENT_TOKEN',
    site: 'datadoghq.com',
    service: 'your-web-application',
    env: 'production',
    version: '1.0.0',
    sessionSampleRate: 100,
    sessionReplaySampleRate: 20,
    trackUserInteractions: true,
    trackResources: true,
    trackLongTasks: true,
    defaultPrivacyLevel: 'mask-user-input',
    allowedTracingUrls: [
        'https://api.yourapp.com',
        'https://api2.yourapp.com'
    ]
});
```

**CDN Initialization:**
```html
<script>
    (function(h,o,u,n,d) {
        h=h[d]=h[d]||{q:[],onReady:function(c){h.q.push(c)}}
        d=o.createElement(u);d.async=1;d.src=n
        n=o.getElementsByTagName(u)[0];n.parentNode.insertBefore(d,n)
    })(window,document,'script','https://www.datadoghq-browser-agent.com/datadog-rum.js','DD_RUM')

    DD_RUM.onReady(function() {
        DD_RUM.init({
            applicationId: 'YOUR_APPLICATION_ID',
            clientToken: 'YOUR_CLIENT_TOKEN',
            site: 'datadoghq.com',
            service: 'your-web-application',
            env: 'production',
            version: '1.0.0',
            sessionSampleRate: 100,
            sessionReplaySampleRate: 20,
            trackUserInteractions: true,
            trackResources: true,
            trackLongTasks: true,
            defaultPrivacyLevel: 'mask-user-input'
        })
    })
</script>
```

### RUM Initialization Configuration

#### Essential Configuration Options

```javascript
datadogRum.init({
    // Required configuration
    applicationId: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
    clientToken: 'dd_client_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    site: 'datadoghq.com', // or 'datadoghq.eu' for EU
    
    // Application metadata
    service: 'frontend-web-app',
    env: 'production',
    version: '1.2.3',
    
    // Data collection settings
    sessionSampleRate: 100,        // Percentage of sessions to track (0-100)
    sessionReplaySampleRate: 20,   // Percentage of sessions for replay (0-100)
    
    // Feature toggles
    trackUserInteractions: true,   // Track clicks, form inputs, taps
    trackResources: true,          // Track resource loading
    trackLongTasks: true,          // Track long running tasks
    trackFrustrations: true,       // Track user frustration signals
    
    // Privacy settings
    defaultPrivacyLevel: 'mask-user-input', // 'allow', 'mask', 'mask-user-input'
    
    // Tracing configuration
    allowedTracingUrls: [
        {
            match: 'https://api.yourapp.com',
            propagatorTypes: ['tracecontext', 'datadog']
        }
    ],
    
    // Custom configuration
    beforeSend: (event) => {
        // Filter or modify events before sending
        if (event.type === 'error' && event.error.isTrusted === false) {
            return false; // Drop untrusted errors
        }
        return true;
    }
});
```

#### Advanced Configuration Options

```javascript
datadogRum.init({
    // Performance monitoring
    premiumSampleRate: 10,         // Premium features sampling (0-100)
    enablePrivacyForActionName: true, // Hide PII in action names
    
    // Custom context
    context: {
        userId: getCurrentUserId(),
        userRole: getCurrentUserRole(),
        accountType: getCurrentAccountType()
    },
    
    // Error tracking
    trackErrors: true,
    defaultErrorCode: 'UNKNOWN',
    
    // Resource tracking
    resourceSampleRate: 100,
    allowFallbackToLocalStorage: true,
    
    // Session management
    sessionReplaySampleRate: 20,
    replaySampleRate: 20,
    
    // Feature flags
    enableBeforeSendAfter: true,
    usePartitionedCrossSiteSessionCookie: false
});
```

### Custom Metrics and Attributes Configuration

#### Adding Custom Attributes

```javascript
// Add global context (applies to all events)
datadogRum.setGlobalContext({
    userId: 'user123',
    userRole: 'premium',
    campaign: 'black-friday-2023',
    featureFlags: ['new-checkout-flow', 'beta-analytics']
});

// Add user information
datadogRum.setUser({
    id: 'user123',
    name: 'John Doe',
    email: 'john.doe@example.com',
    plan: 'premium',
    organization: 'Acme Corp'
});

// Add custom attributes to specific events
datadogRum.addTiming('custom_checkout_timing');
```

#### Custom Metrics Collection

```javascript
// Track custom timing metrics
function trackCustomTiming(name, startTime) {
    const endTime = performance.now();
    const duration = endTime - startTime;
    
    datadogRum.addTiming(name);
    
    // Add custom attributes
    datadogRum.setGlobalContextProperty('custom_timing', {
        name: name,
        duration: duration,
        timestamp: Date.now()
    });
}

// Track custom events
function trackCustomEvent(eventName, eventData) {
    datadogRum.addAction(eventName, eventData);
}

// Example usage
const checkoutStartTime = performance.now();
// ... checkout process ...
trackCustomTiming('checkout_completion', checkoutStartTime);

trackCustomEvent('feature_used', {
    feature_name: 'advanced_search',
    search_query: 'datadog monitoring',
    results_count: 25
});
```

### Environment Setup (Dev, Staging, Production)

#### Environment-Specific Configuration

```javascript
// Environment configuration
const getRumConfig = () => {
    const configs = {
        development: {
            applicationId: 'dev-app-id',
            clientToken: 'dev-client-token',
            env: 'development',
            sessionSampleRate: 100,
            sessionReplaySampleRate: 100,
            trackErrors: true,
            debug: true
        },
        staging: {
            applicationId: 'staging-app-id',
            clientToken: 'staging-client-token',
            env: 'staging',
            sessionSampleRate: 50,
            sessionReplaySampleRate: 10,
            trackErrors: true,
            debug: false
        },
        production: {
            applicationId: 'prod-app-id',
            clientToken: 'prod-client-token',
            env: 'production',
            sessionSampleRate: 20,
            sessionReplaySampleRate: 5,
            trackErrors: true,
            debug: false
        }
    };
    
    return configs[process.env.NODE_ENV] || configs.development;
};

// Initialize based on environment
const rumConfig = getRumConfig();
datadogRum.init(rumConfig);
```

#### Environment Detection and Auto-Configuration

```javascript
// Automatic environment detection
function detectEnvironment() {
    const hostname = window.location.hostname;
    
    if (hostname.includes('localhost') || hostname.includes('127.0.0.1')) {
        return 'development';
    } else if (hostname.includes('staging') || hostname.includes('test')) {
        return 'staging';
    } else {
        return 'production';
    }
}

// Dynamic configuration loading
async function loadRumConfiguration() {
    const environment = detectEnvironment();
    
    try {
        const response = await fetch(`/config/rum-${environment}.json`);
        const config = await response.json();
        return config;
    } catch (error) {
        console.warn('Failed to load RUM config, using defaults:', error);
        return getRumConfig();
    }
}

// Initialize with dynamic configuration
loadRumConfiguration().then(rumConfig => {
    datadogRum.init(rumConfig);
});
```

## Website Monitoring with DataDog RUM

### Page Load Performance Monitoring (Core Web Vitals)

#### Automatic Core Web Vitals Collection

DataDog RUM automatically collects and reports on all Core Web Vitals:

```javascript
// DataDog automatically tracks:
// - Largest Contentful Paint (LCP)
// - First Input Delay (FID) 
// - Cumulative Layout Shift (CLS)

// View performance in DataDog dashboard:
// - Performance > Core Web Vitals
// - Filter by service, environment, or custom tags

// Custom performance monitoring
datadogRum.onReady(() => {
    // Get current performance metrics
    const performance = datadogRum.getInternalContext();
    
    console.log('Current session ID:', performance.sessionId);
    console.log('View ID:', performance.view.id);
});
```

#### Custom Performance Metrics

```javascript
// Track custom performance metrics
function trackPagePerformance() {
    // Measure Time to Interactive (TTI)
    const measureTTI = () => {
        const observer = new PerformanceObserver((list) => {
            for (const entry of list.getEntries()) {
                if (entry.entryType === 'first-input') {
                    datadogRum.addAction('time_to_interactive', {
                        duration: entry.startTime,
                        type: 'performance'
                    });
                    observer.disconnect();
                }
            }
        });
        observer.observe({ entryTypes: ['first-input'] });
    };

    // Measure Time to First Byte (TTFB)
    const measureTTFB = () => {
        const navigation = performance.getEntriesByType('navigation')[0];
        if (navigation) {
            datadogRum.addAction('time_to_first_byte', {
                duration: navigation.responseStart - navigation.requestStart,
                type: 'performance'
            });
        }
    };

    // Measure Custom Metrics
    const measureCustomMetrics = () => {
        // Custom loading phases
        const phases = {
            'app_loaded': () => window.appLoaded,
            'data_fetched': () => window.dataFetched,
            'ui_ready': () => window.uiReady
        };

        Object.entries(phases).forEach(([phase, checkFn]) => {
            const startTime = performance.now();
            
            const checkInterval = setInterval(() => {
                if (checkFn()) {
                    const duration = performance.now() - startTime;
                    datadogRum.addAction(`phase_${phase}`, {
                        duration: duration,
                        type: 'custom_performance'
                    });
                    clearInterval(checkInterval);
                }
            }, 100);
        });
    };

    measureTTI();
    measureTTFB();
    measureCustomMetrics();
}

// Initialize performance tracking
trackPagePerformance();
```

#### Performance Budget Monitoring

```javascript
// Set up performance budgets
const performanceBudgets = {
    lcp: 2500,      // 2.5 seconds
    fid: 100,       // 100ms
    cls: 0.1,       // 0.1
    ttfb: 500,      // 500ms
    custom_load: 3000 // 3 seconds
};

function checkPerformanceBudgets() {
    // Monitor LCP budget
    const lcpObserver = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        
        if (lastEntry.startTime > performanceBudgets.lcp) {
            datadogRum.addError(new Error('LCP budget exceeded'), {
                budget: 'lcp',
                actual: lastEntry.startTime,
                limit: performanceBudgets.lcp,
                severity: 'warning'
            });
        }
    });
    lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });

    // Monitor FID budget
    const fidObserver = new PerformanceObserver((list) => {
        list.getEntries().forEach((entry) => {
            if ((entry.processingStart - entry.startTime) > performanceBudgets.fid) {
                datadogRum.addError(new Error('FID budget exceeded'), {
                    budget: 'fid',
                    actual: entry.processingStart - entry.startTime,
                    limit: performanceBudgets.fid,
                    severity: 'warning'
                });
            }
        });
    });
    fidObserver.observe({ entryTypes: ['first-input'] });
}

checkPerformanceBudgets();
```

### API Endpoint Monitoring and Error Tracking

#### Automatic API Monitoring

```javascript
// DataDog automatically tracks all XHR and fetch requests
// Configure tracing for your API endpoints

datadogRum.init({
    // ... other config ...
    allowedTracingUrls: [
        {
            match: 'https://api.yourapp.com',
            propagatorTypes: ['tracecontext', 'datadog']
        },
        {
            match: 'https://internal-api.yourapp.com',
            propagatorTypes: ['datadog']
        }
    ],
    traceSampleRate: 100
});

// Track custom API metrics
function trackApiCall(endpoint, method, startTime, response) {
    const duration = performance.now() - startTime;
    
    datadogRum.addAction('api_call', {
        endpoint: endpoint,
        method: method,
        status: response.status,
        duration: duration,
        success: response.ok,
        size: response.headers.get('content-length') || 0
    });
    
    // Track errors
    if (!response.ok) {
        datadogRum.addError(new Error(`API Error: ${response.status}`), {
            endpoint: endpoint,
            method: method,
            status: response.status,
            duration: duration
        });
    }
}

// Enhanced fetch wrapper
const originalFetch = window.fetch;
window.fetch = async function(url, options = {}) {
    const startTime = performance.now();
    const method = options.method || 'GET';
    
    try {
        const response = await originalFetch.apply(this, arguments);
        trackApiCall(url, method, startTime, response);
        return response;
    } catch (error) {
        trackApiCall(url, method, startTime, { ok: false, status: 0 });
        throw error;
    }
};
```

#### Custom API Error Tracking

```javascript
// Comprehensive API error tracking
class ApiErrorTracker {
    constructor() {
        this.errorCounts = new Map();
        this.lastErrorTime = new Map();
        this.rateLimitWindow = 60000; // 1 minute
    }
    
    trackApiError(error, endpoint, method) {
        const key = `${endpoint}:${method}`;
        const now = Date.now();
        
        // Update error counts
        if (!this.errorCounts.has(key)) {
            this.errorCounts.set(key, []);
        }
        
        const errors = this.errorCounts.get(key);
        errors.push(now);
        
        // Clean old errors outside window
        const recentErrors = errors.filter(time => now - time < this.rateLimitWindow);
        this.errorCounts.set(key, recentErrors);
        
        // Track in DataDog
        datadogRum.addError(error, {
            endpoint: endpoint,
            method: method,
            error_count: recentErrors.length,
            error_type: this.categorizeError(error),
            timestamp: now
        });
        
        // Alert on high error rates
        if (recentErrors.length >= 5) {
            this.sendAlert(key, recentErrors.length, endpoint);
        }
    }
    
    categorizeError(error) {
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
            return 'network_error';
        } else if (error.message.includes('4')) {
            return 'client_error';
        } else if (error.message.includes('5')) {
            return 'server_error';
        } else {
            return 'unknown_error';
        }
    }
    
    sendAlert(key, count, endpoint) {
        const lastAlert = this.lastErrorTime.get(key);
        const now = Date.now();
        
        // Rate limit alerts to once per 5 minutes
        if (!lastAlert || now - lastAlert > 300000) {
            datadogRum.addError(new Error(`High error rate detected: ${count} errors in 1 minute`), {
                alert_type: 'high_error_rate',
                endpoint: endpoint,
                error_count: count,
                severity: 'critical'
            });
            
            this.lastErrorTime.set(key, now);
        }
    }
}

// Initialize API error tracking
const apiErrorTracker = new ApiErrorTracker();

// Track fetch errors
window.addEventListener('unhandledrejection', (event) => {
    if (event.reason && event.reason.url) {
        apiErrorTracker.trackApiError(
            event.reason,
            event.reason.url,
            event.reason.config?.method || 'GET'
        );
    }
});
```

### Resource Loading Performance

#### Resource Monitoring

```javascript
// Monitor resource loading performance
class ResourceMonitor {
    constructor() {
        this.resourceTimings = new Map();
        this.setupResourceObserver();
    }
    
    setupResourceObserver() {
        const observer = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            
            entries.forEach((entry) => {
                if (entry.initiatorType && entry.duration > 0) {
                    this.analyzeResource(entry);
                }
            });
        });
        
        observer.observe({ entryTypes: ['resource'] });
    }
    
    analyzeResource(entry) {
        const resourceData = {
            name: entry.name,
            type: entry.initiatorType,
            duration: entry.duration,
            transferSize: entry.transferSize,
            encodedBodySize: entry.encodedBodySize,
            decodedBodySize: entry.decodedBodySize,
            startTime: entry.startTime,
            timestamp: Date.now()
        };
        
        // Track in DataDog
        datadogRum.addAction('resource_load', resourceData);
        
        // Check for slow resources
        if (entry.duration > 1000) {
            datadogRum.addError(new Error(`Slow resource: ${entry.name}`), {
                resource_name: entry.name,
                resource_type: entry.initiatorType,
                duration: entry.duration,
                threshold: 1000
            });
        }
        
        // Track critical resources separately
        if (this.isCriticalResource(entry.name)) {
            datadogRum.addAction('critical_resource_load', {
                ...resourceData,
                is_critical: true
            });
        }
    }
    
    isCriticalResource(url) {
        const criticalPatterns = [
            /\.css$/,
            /\.js$/,
            /critical/,
            /bundle/,
            /main/
        ];
        
        return criticalPatterns.some(pattern => pattern.test(url));
    }
    
    getResourceSummary() {
        const summary = {
            total: 0,
            byType: {},
            slowResources: [],
            totalLoadTime: 0
        };
        
        // Get all resource entries
        const resources = performance.getEntriesByType('resource');
        
        resources.forEach(resource => {
            summary.total++;
            summary.totalLoadTime += resource.duration;
            
            if (!summary.byType[resource.initiatorType]) {
                summary.byType[resource.initiatorType] = {
                    count: 0,
                    totalDuration: 0,
                    averageDuration: 0
                };
            }
            
            summary.byType[resource.initiatorType].count++;
            summary.byType[resource.initiatorType].totalDuration += resource.duration;
            
            if (resource.duration > 1000) {
                summary.slowResources.push({
                    name: resource.name,
                    duration: resource.duration,
                    type: resource.initiatorType
                });
            }
        });
        
        // Calculate averages
        Object.values(summary.byType).forEach(type => {
            type.averageDuration = type.totalDuration / type.count;
        });
        
        return summary;
    }
}

// Initialize resource monitoring
const resourceMonitor = new ResourceMonitor();

// Track resource summary periodically
setInterval(() => {
    const summary = resourceMonitor.getResourceSummary();
    datadogRum.addAction('resource_summary', summary);
}, 30000); // Every 30 seconds
```

### User Session Replay and Analytics

#### Session Replay Configuration

```javascript
// Configure session replay
datadogRum.init({
    // ... other config ...
    sessionReplaySampleRate: 20,    // 20% of sessions
    trackUserInteractions: true,    // Track clicks, inputs, taps
    trackFrustrations: true,        // Track rage clicks, dead clicks
    defaultPrivacyLevel: 'mask-user-input', // Mask sensitive input
    enablePrivacyForActionName: true, // Hide PII in action names
    trackResources: true,
    trackLongTasks: true
});

// Add session context
datadogRum.setUser({
    id: getCurrentUserId(),
    name: getCurrentUserName(),
    email: getCurrentUserEmail(),
    role: getCurrentUserRole(),
    account_id: getCurrentAccountId()
});

// Track custom session events
function trackUserJourney(step, data = {}) {
    datadogRum.addAction(`user_journey_${step}`, {
        journey_step: step,
        ...data,
        timestamp: Date.now()
    });
}

// Example usage in user flows
function trackCheckoutFlow(step) {
    const journeyData = {
        step: step,
        cart_value: getCurrentCartValue(),
        items_count: getCartItemCount(),
        payment_method: getSelectedPaymentMethod()
    };
    
    trackUserJourney('checkout', journeyData);
}

// Track feature adoption
function trackFeatureAdoption(featureName, context = {}) {
    datadogRum.addAction('feature_adoption', {
        feature_name: featureName,
        adoption_type: 'first_use',
        ...context,
        timestamp: Date.now()
    });
}
```

### Error Tracking and Debugging

#### Comprehensive Error Tracking

```javascript
// Enhanced error tracking setup
class EnhancedErrorTracker {
    constructor() {
        this.setupGlobalErrorHandlers();
        this.setupUnhandledRejectionHandler();
        this.setupResourceErrorHandler();
        this.errorCounts = new Map();
    }
    
    setupGlobalErrorHandlers() {
        // JavaScript errors
        window.addEventListener('error', (event) => {
            this.trackError({
                type: 'javascript',
                message: event.message,
                filename: event.filename,
                lineno: event.lineno,
                colno: event.colno,
                error: event.error,
                timestamp: Date.now(),
                userAgent: navigator.userAgent,
                url: window.location.href
            });
        });
    }
    
    setupUnhandledRejectionHandler() {
        // Unhandled promise rejections
        window.addEventListener('unhandledrejection', (event) => {
            this.trackError({
                type: 'promise',
                message: event.reason?.message || 'Unhandled Promise Rejection',
                reason: event.reason,
                stack: event.reason?.stack,
                timestamp: Date.now(),
                userAgent: navigator.userAgent,
                url: window.location.href
            });
        });
    }
    
    setupResourceErrorHandler() {
        // Resource loading errors
        window.addEventListener('error', (event) => {
            if (event.target && (event.target.tagName === 'SCRIPT' || 
                event.target.tagName === 'LINK' || 
                event.target.tagName === 'IMG' ||
                event.target.tagName === 'LINK')) {
                
                this.trackError({
                    type: 'resource',
                    message: event.message,
                    target: event.target.tagName.toLowerCase(),
                    src: event.target.src || event.target.href,
                    timestamp: Date.now(),
                    url: window.location.href
                });
            }
        }, true);
    }
    
    trackError(errorData) {
        // Add error ID and categorize
        errorData.id = this.generateErrorId();
        errorData.category = this.categorizeError(errorData);
        errorData.severity = this.calculateSeverity(errorData);
        
        // Count errors for rate limiting
        const errorKey = `${errorData.type}:${errorData.category}`;
        const count = (this.errorCounts.get(errorKey) || 0) + 1;
        this.errorCounts.set(errorKey, count);
        
        // Add to DataDog
        datadogRum.addError(
            new Error(`${errorData.type}: ${errorData.message}`),
            {
                ...errorData,
                error_count: count,
                user_session: datadogRum.getInternalContext()?.sessionId,
                page_url: window.location.pathname,
                user_agent: navigator.userAgent,
                timestamp: Date.now()
            }
        );
        
        // Log for development
        if (process.env.NODE_ENV === 'development') {
            console.error('Enhanced error tracked:', errorData);
        }
    }
    
    categorizeError(errorData) {
        if (errorData.type === 'javascript') {
            if (errorData.message.includes('NetworkError') || 
                errorData.message.includes('fetch')) {
                return 'network';
            } else if (errorData.message.includes('ReferenceError')) {
                return 'reference';
            } else if (errorData.message.includes('TypeError')) {
                return 'type';
            } else {
                return 'general';
            }
        } else if (errorData.type === 'resource') {
            return errorData.target || 'unknown';
        } else if (errorData.type === 'promise') {
            return 'async';
        }
        
        return 'unknown';
    }
    
    calculateSeverity(errorData) {
        // Calculate error severity based on type and context
        if (errorData.type === 'javascript') {
            if (errorData.category === 'network') return 'high';
            if (errorData.category === 'reference') return 'medium';
            return 'low';
        }
        
        return 'medium';
    }
    
    generateErrorId() {
        return `err_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    
    getErrorSummary() {
        const summary = {
            totalErrors: Array.from(this.errorCounts.values()).reduce((a, b) => a + b, 0),
            byCategory: {},
            recentErrors: [],
            trends: this.analyzeErrorTrends()
        };
        
        this.errorCounts.forEach((count, key) => {
            const [type, category] = key.split(':');
            if (!summary.byCategory[type]) {
                summary.byCategory[type] = {};
            }
            summary.byCategory[type][category] = count;
        });
        
        return summary;
    }
    
    analyzeErrorTrends() {
        // Analyze error patterns over time
        return {
            totalErrors: Array.from(this.errorCounts.values()).reduce((a, b) => a + b, 0),
            mostCommon: Array.from(this.errorCounts.entries())
                .sort((a, b) => b[1] - a[1])[0],
            errorRate: this.calculateErrorRate()
        };
    }
    
    calculateErrorRate() {
        // Calculate errors per minute
        const totalErrors = Array.from(this.errorCounts.values()).reduce((a, b) => a + b, 0);
        const timeWindow = 5 * 60 * 1000; // 5 minutes
        return Math.round((totalErrors / timeWindow) * 60000); // errors per minute
    }
}

// Initialize enhanced error tracking
const enhancedErrorTracker = new EnhancedErrorTracker();

// Track error summary periodically
setInterval(() => {
    const summary = enhancedErrorTracker.getErrorSummary();
    datadogRum.addAction('error_summary', summary);
}, 60000); // Every minute
```

## DataDog Dashboard Creation

### Dashboard Widgets for Website Monitoring

#### Creating Custom Dashboards

DataDog RUM provides powerful dashboard capabilities for visualizing your website performance data:

**1. Core Web Vitals Dashboard:**
- LCP, FID, CLS trends over time
- Performance by page URL
- Geographic performance distribution
- Device and browser performance comparison

**2. User Experience Dashboard:**
- Session replay availability
- User interaction patterns
- Page views and unique visitors
- Conversion funnel tracking

**3. Error Monitoring Dashboard:**
- Error rates by type and severity
- Error frequency over time
- Top error-prone pages
- Error correlation with performance metrics

#### Custom Dashboard Configuration

```json
{
  "title": "Website Performance Dashboard",
  "description": "Comprehensive website monitoring using DataDog RUM",
  "widgets": [
    {
      "id": 1,
      "layout": { "x": 0, "y": 0, "width": 4, "height": 3 },
      "definition": {
        "title": "Core Web Vitals - LCP",
        "type": "timeseries",
        "requests": [
          {
            "q": "rum.custom.lcp{*} by {env,service}",
            "aggregator": "avg",
            "conditional_formats": [
              {
                "palette": "red",
                "comparator": ">",
                "value": 2500
              },
              {
                "palette": "yellow", 
                "comparator": ">",
                "value": 1500
              }
            ]
          }
        ],
        "yaxis": {
          "label": "LCP (ms)",
          "min": 0,
          "max": 4000
        }
      }
    },
    {
      "id": 2,
      "layout": { "x": 4, "y": 0, "width": 4, "height": 3 },
      "definition": {
        "title": "Error Rate",
        "type": "timeseries",
        "requests": [
          {
            "q": "rum.error{*} by {env,service}.as_count()",
            "aggregator": "sum"
          }
        ],
        "yaxis": {
          "label": "Errors per minute",
          "min": 0
        }
      }
    },
    {
      "id": 3,
      "layout": { "x": 8, "y": 0, "width": 4, "height": 3 },
      "definition": {
        "title": "Page Views",
        "type": "timeseries",
        "requests": [
          {
            "q": "rum.view{*} by {env,service}.as_count()",
            "aggregator": "sum"
          }
        ],
        "yaxis": {
          "label": "Page views per minute",
          "min": 0
        }
      }
    }
  ],
  "template_variables": [
    {
      "name": "env",
      "default": "production",
      "options": ["development", "staging", "production"]
    },
    {
      "name": "service",
      "default": "frontend-web-app",
      "options": ["frontend-web-app", "mobile-app", "admin-panel"]
    }
  ],
  "layout_type": "ordered",
  "is_read_only": false
}
```

#### Performance Monitoring Widgets

```javascript
// Dashboard widget configurations for API integration

const performanceWidgets = {
    // Core Web Vitals Overview
    coreWebVitals: {
        title: "Core Web Vitals Overview",
        type: "query_table",
        requests: [
            {
                q: "avg:rum.lcp{*} by {env,service}",
                alias: "LCP (ms)"
            },
            {
                q: "avg:rum.fid{*} by {env,service}", 
                alias: "FID (ms)"
            },
            {
                q: "avg:rum.cls{*} by {env,service}",
                alias: "CLS"
            }
        ],
        formulas: [
            {
                formula: "LCP < 2500 ? 'Good' : (LCP < 4000 ? 'Needs Improvement' : 'Poor')",
                alias: "LCP Status"
            },
            {
                formula: "FID < 100 ? 'Good' : (FID < 300 ? 'Needs Improvement' : 'Poor')",
                alias: "FID Status"
            },
            {
                formula: "CLS < 0.1 ? 'Good' : (CLS < 0.25 ? 'Needs Improvement' : 'Poor')",
                alias: "CLS Status"
            }
        ]
    },
    
    // API Performance
    apiPerformance: {
        title: "API Performance Metrics",
        type: "timeseries",
        requests: [
            {
                q: "avg:rum.resource.duration{type:fetch} by {env,service,endpoint}",
                aggregator: "avg",
                style: {
                    palette: "dog_classic",
                    line_type: "solid",
                    line_width: "normal"
                }
            }
        ],
        yaxis: {
            label: "Response Time (ms)",
            min: 0
        }
    },
    
    // User Engagement
    userEngagement: {
        title: "User Engagement Metrics",
        type: "timeseries",
        requests: [
            {
                q: "sum:rum.view{*} by {env,service}",
                aggregator: "sum",
                style: {
                    palette: "green",
                    line_type: "solid"
                }
            },
            {
                q: "sum:rum.action{*} by {env,service}",
                aggregator: "sum",
                style: {
                    palette: "blue",
                    line_type: "dashed"
                }
            }
        ],
        yaxis: {
            label: "Count",
            min: 0
        }
    }
};
```

### Custom Metrics Visualization

#### Creating Custom Metrics

```javascript
// Define custom metrics in your application
function createCustomMetrics() {
    // Business metrics
    const businessMetrics = {
        // Conversion tracking
        trackConversion: (conversionType, value) => {
            datadogRum.addAction('conversion', {
                conversion_type: conversionType,
                conversion_value: value,
                currency: 'USD',
                timestamp: Date.now()
            });
        },
        
        // Feature usage tracking
        trackFeatureUsage: (featureName, usageData) => {
            datadogRum.addAction('feature_usage', {
                feature_name: featureName,
                ...usageData,
                timestamp: Date.now()
            });
        },
        
        // Custom performance metrics
        trackCustomPerformance: (metricName, value, unit) => {
            datadogRum.addAction('custom_performance', {
                metric_name: metricName,
                metric_value: value,
                metric_unit: unit,
                timestamp: Date.now()
            });
        }
    };
    
    return businessMetrics;
}

// Usage examples
const metrics = createCustomMetrics();

// Track conversions
metrics.trackConversion('signup', 0);
metrics.trackConversion('purchase', 29.99);

// Track feature usage
metrics.trackFeatureUsage('advanced_search', {
    search_query: 'datadog rum',
    results_count: 15,
    filters_applied: 3
});

// Track custom performance
metrics.trackCustomPerformance('checkout_completion_time', 4500, 'ms');
metrics.trackCustomPerformance('data_sync_time', 2.5, 'seconds');
```

#### Custom Dashboard API

```javascript
// Create dashboards programmatically using DataDog API
const dashboardApi = {
    // Create a new dashboard
    createDashboard: async (dashboardConfig) => {
        const response = await fetch('https://api.datadoghq.com/api/v1/dashboard', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'DD-API-KEY': 'YOUR_API_KEY',
                'DD-APPLICATION-KEY': 'YOUR_APPLICATION_KEY'
            },
            body: JSON.stringify(dashboardConfig)
        });
        
        if (!response.ok) {
            throw new Error(`Failed to create dashboard: ${response.statusText}`);
        }
        
        return await response.json();
    },
    
    // Update existing dashboard
    updateDashboard: async (dashboardId, dashboardConfig) => {
        const response = await fetch(`https://api.datadoghq.com/api/v1/dashboard/${dashboardId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'DD-API-KEY': 'YOUR_API_KEY',
                'DD-APPLICATION-KEY': 'YOUR_APPLICATION_KEY'
            },
            body: JSON.stringify(dashboardConfig)
        });
        
        if (!response.ok) {
            throw new Error(`Failed to update dashboard: ${response.statusText}`);
        }
        
        return await response.json();
    },
    
    // Get dashboard by ID
    getDashboard: async (dashboardId) => {
        const response = await fetch(`https://api.datadoghq.com/api/v1/dashboard/${dashboardId}`, {
            headers: {
                'DD-API-KEY': 'YOUR_API_KEY',
                'DD-APPLICATION-KEY': 'YOUR_APPLICATION_KEY'
            }
        });
        
        if (!response.ok) {
            throw new Error(`Failed to get dashboard: ${response.statusText}`);
        }
        
        return await response.json();
    }
};

// Example dashboard creation
const createWebsiteMonitoringDashboard = async () => {
    const dashboardConfig = {
        title: "Website Performance Monitoring",
        description: "Real-time website performance and user experience monitoring",
        widgets: [
            // Core Web Vitals widget
            {
                layout: { x: 0, y: 0, width: 6, height: 4 },
                definition: {
                    title: "Core Web Vitals",
                    type: "timeseries",
                    requests: [
                        {
                            q: "avg:rum.lcp{*} by {env,service}",
                            aggregator: "avg"
                        },
                        {
                            q: "avg:rum.fid{*} by {env,service}",
                            aggregator: "avg"
                        },
                        {
                            q: "avg:rum.cls{*} by {env,service}",
                            aggregator: "avg"
                        }
                    ]
                }
            },
            
            // Error rate widget
            {
                layout: { x: 6, y: 0, width: 6, height: 4 },
                definition: {
                    title: "Error Rate",
                    type: "timeseries",
                    requests: [
                        {
                            q: "sum:rum.error{*} by {env,service}",
                            aggregator: "sum"
                        }
                    ]
                }
            }
        ],
        template_variables: [
            {
                name: "env",
                default: "production",
                options: ["development", "staging", "production"]
            },
            {
                name: "service",
                default: "frontend-web-app",
                options: ["frontend-web-app", "mobile-app"]
            }
        ],
        layout_type: "ordered",
        is_read_only: false
    };
    
    try {
        const result = await dashboardApi.createDashboard(dashboardConfig);
        console.log('Dashboard created successfully:', result.url);
        return result;
    } catch (error) {
        console.error('Failed to create dashboard:', error);
        throw error;
    }
};
```

### Alerting Configuration

#### Setting Up Alerts

DataDog RUM provides powerful alerting capabilities to notify you of performance issues:

```javascript
// Alert configuration examples

const alertRules = {
    // Core Web Vitals alerts
    coreWebVitals: [
        {
            name: "LCP Performance Alert",
            message: "LCP is exceeding the performance threshold",
            query: "avg(last_5m):avg:rum.lcp{*} > 2500",
            thresholds: {
                critical: 2500,
                warning: 2000
            },
            tags: ["team:frontend", "service:web-app"],
            priority: 1
        },
        {
            name: "FID Performance Alert", 
            message: "First Input Delay is too high",
            query: "avg(last_5m):avg:rum.fid{*} > 100",
            thresholds: {
                critical: 100,
                warning: 80
            },
            tags: ["team:frontend", "service:web-app"],
            priority: 2
        },
        {
            name: "CLS Performance Alert",
            message: "Cumulative Layout Shift is too high",
            query: "avg(last_5m):avg:rum.cls{*} > 0.1",
            thresholds: {
                critical: 0.1,
                warning: 0.05
            },
            tags: ["team:frontend", "service:web-app"],
            priority: 3
        }
    ],
    
    // Error rate alerts
    errorRate: [
        {
            name: "High Error Rate Alert",
            message: "Error rate is exceeding acceptable levels",
            query: "sum(last_5m):sum:rum.error{*} > 100",
            thresholds: {
                critical: 100,
                warning: 50
            },
            tags: ["team:frontend", "service:web-app"],
            priority: 1
        },
        {
            name: "JavaScript Error Alert",
            query: "sum(last_5m):sum:rum.error{type:javascript} > 50",
            thresholds: {
                critical: 50,
                warning: 25
            },
            tags: ["team:frontend", "service:web-app"],
            priority: 2
        }
    ],
    
    // User experience alerts
    userExperience: [
        {
            name: "Low Page Views Alert",
            message: "Page views have dropped significantly",
            query: "sum(last_10m):sum:rum.view{*} < 100",
            thresholds: {
                critical: 100,
                warning: 150
            },
            tags: ["team:product", "service:web-app"],
            priority: 3
        }
    ]
};

// Create alerts programmatically
const alertApi = {
    createAlert: async (alertConfig) => {
        const response = await fetch('https://api.datadoghq.com/api/v1/monitor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'DD-API-KEY': 'YOUR_API_KEY',
                'DD-APPLICATION-KEY': 'YOUR_APPLICATION_KEY'
            },
            body: JSON.stringify(alertConfig)
        });
        
        if (!response.ok) {
            throw new Error(`Failed to create alert: ${response.statusText}`);
        }
        
        return await response.json();
    },
    
    createAllAlerts: async () => {
        const allAlerts = [
            ...alertRules.coreWebVitals,
            ...alertRules.errorRate,
            ...alertRules.userExperience
        ];
        
        const results = [];
        
        for (const alertConfig of allAlerts) {
            try {
                const result = await alertApi.createAlert(alertConfig);
                results.push({ success: true, config: alertConfig, result });
            } catch (error) {
                results.push({ success: false, config: alertConfig, error: error.message });
            }
        }
        
        return results;
    }
};
```

#### Alert Integration with External Systems

```javascript
// Integrate DataDog alerts with external systems

const alertIntegrations = {
    // Slack integration
    slack: {
        webhookUrl: 'https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK',
        
        sendSlackAlert: async (alertData) => {
            const message = {
                text: `:warning: DataDog Alert: ${alertData.title}`,
                attachments: [
                    {
                        color: alertData.priority === 'critical' ? 'danger' : 'warning',
                        fields: [
                            {
                                title: 'Alert',
                                value: alertData.message,
                                short: false
                            },
                            {
                                title: 'Environment',
                                value: alertData.env || 'unknown',
                                short: true
                            },
                            {
                                title: 'Service',
                                value: alertData.service || 'unknown',
                                short: true
                            },
                            {
                                title: 'Severity',
                                value: alertData.priority || 'unknown',
                                short: true
                            }
                        ]
                    }
                ]
            };
            
            await fetch(this.webhookUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(message)
            });
        }
    },
    
    // Email integration
    email: {
        sendGridApiKey: 'YOUR_SENDGRID_API_KEY',
        
        sendEmailAlert: async (alertData, recipients) => {
            const email = {
                personalizations: [
                    {
                        to: recipients.map(email => ({ email })),
                        subject: `DataDog Alert: ${alertData.title}`
                    }
                ],
                from: { email: 'alerts@yourapp.com' },
                content: [
                    {
                        type: 'text/html',
                        value: `
                            <h2>DataDog Alert</h2>
                            <p><strong>Alert:</strong> ${alertData.title}</p>
                            <p><strong>Message:</strong> ${alertData.message}</p>
                            <p><strong>Environment:</strong> ${alertData.env}</p>
                            <p><strong>Service:</strong> ${alertData.service}</p>
                            <p><strong>Severity:</strong> ${alertData.priority}</p>
                            <p><strong>Timestamp:</strong> ${new Date(alertData.timestamp).toISOString()}</p>
                        `
                    }
                ]
            };
            
            await fetch('https://api.sendgrid.com/v3/mail/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.sendGridApiKey}`
                },
                body: JSON.stringify(email)
            });
        }
    },
    
    // PagerDuty integration
    pagerDuty: {
        integrationKey: 'YOUR_PAGERDUTY_INTEGRATION_KEY',
        
        sendPagerDutyAlert: async (alertData) => {
            const incident = {
                routing_key: this.integrationKey,
                event_action: 'trigger',
                dedup_key: `datadog-${alertData.id}`,
                payload: {
                    summary: `${alertData.title}: ${alertData.message}`,
                    source: 'DataDog RUM',
                    severity: alertData.priority === 'critical' ? 'critical' : 'error',
                    component: alertData.service,
                    group: alertData.env,
                    class: 'performance',
                    custom_details: {
                        alert_id: alertData.id,
                        query: alertData.query,
                        value: alertData.value,
                        threshold: alertData.threshold
                    }
                }
            };
            
            await fetch('https://events.pagerduty.com/v2/enqueue', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(incident)
            });
        }
    }
};
```

## Implementation Examples

### DataDog RUM JavaScript SDK Integration

#### Basic Integration

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Web Application</title>
</head>
<body>
    <!-- Your application content -->
    
    <!-- DataDog RUM SDK -->
    <script src="https://www.datadoghq-browser-agent.com/datadog-rum.js"></script>
    <script>
        // Initialize DataDog RUM
        (function() {
            // Configuration based on environment
            const config = {
                development: {
                    applicationId: 'dev-application-id',
                    clientToken: 'dev-client-token',
                    env: 'development',
                    sessionSampleRate: 100,
                    sessionReplaySampleRate: 100,
                    debug: true
                },
                staging: {
                    applicationId: 'staging-application-id',
                    clientToken: 'staging-client-token', 
                    env: 'staging',
                    sessionSampleRate: 50,
                    sessionReplaySampleRate: 20,
                    debug: false
                },
                production: {
                    applicationId: 'prod-application-id',
                    clientToken: 'prod-client-token',
                    env: 'production',
                    sessionSampleRate: 20,
                    sessionReplaySampleRate: 5,
                    debug: false
                }
            };
            
            // Detect environment
            function getEnvironment() {
                const hostname = window.location.hostname;
                if (hostname.includes('localhost') || hostname.includes('127.0.0.1')) {
                    return 'development';
                } else if (hostname.includes('staging')) {
                    return 'staging';
                } else {
                    return 'production';
                }
            }
            
            const environment = getEnvironment();
            const rumConfig = config[environment];
            
            // Initialize DataDog RUM
            DD_RUM.onReady(function() {
                DD_RUM.init({
                    ...rumConfig,
                    service: 'your-web-application',
                    version: '1.0.0',
                    trackUserInteractions: true,
                    trackResources: true,
                    trackLongTasks: true,
                    trackFrustrations: true,
                    defaultPrivacyLevel: 'mask-user-input',
                    allowedTracingUrls: [
                        'https://api.yourapp.com',
                        'https://internal-api.yourapp.com'
                    ],
                    beforeSend: (event) => {
                        // Filter or modify events before sending
                        if (event.type === 'error' && event.error.isTrusted === false) {
                            return false; // Drop untrusted errors
                        }
                        return true;
                    }
                });
                
                // Set user context if available
                if (window.currentUser) {
                    DD_RUM.setUser({
                        id: window.currentUser.id,
                        name: window.currentUser.name,
                        email: window.currentUser.email,
                        role: window.currentUser.role
                    });
                }
                
                // Add global context
                DD_RUM.setGlobalContext({
                    page_category: window.pageCategory || 'general',
                    campaign: window.campaign || 'organic'
                });
            });
        })();
    </script>
</body>
</html>
```

#### Advanced Integration with React

```javascript
// React integration example
import { useEffect } from 'react';
import { datadogRum } from '@datadog/browser-rum';

// DataDog RUM provider for React
export function DataDogProvider({ children, config }) {
    useEffect(() => {
        // Initialize DataDog RUM
        if (!datadogRum.getInternalContext()) {
            datadogRum.init(config);
        }
        
        // Track route changes
        const originalPushState = history.pushState;
        const originalReplaceState = history.replaceState;
        
        const trackRouteChange = (method) => {
            return function(...args) {
                const url = args[2];
                if (url) {
                    datadogRum.startView({
                        name: document.title,
                        url: url
                    });
                }
                return method.apply(this, args);
            };
        };
        
        history.pushState = trackRouteChange(originalPushState);
        history.replaceState = trackRouteChange(originalReplaceState);
        
        // Track initial view
        datadogRum.startView({
            name: document.title,
            url: window.location.href
        });
        
        return () => {
            history.pushState = originalPushState;
            history.replaceState = originalReplaceState;
        };
    }, [config]);
    
    return children;
}

// Usage in React app
function App() {
    const rumConfig = {
        applicationId: process.env.REACT_APP_DD_APPLICATION_ID,
        clientToken: process.env.REACT_APP_DD_CLIENT_TOKEN,
        site: 'datadoghq.com',
        service: 'react-web-app',
        env: process.env.NODE_ENV,
        version: process.env.REACT_APP_VERSION,
        sessionSampleRate: 100,
        sessionReplaySampleRate: 20,
        trackUserInteractions: true,
        trackResources: true,
        trackLongTasks: true,
        defaultPrivacyLevel: 'mask-user-input'
    };
    
    return (
        <DataDogProvider config={rumConfig}>
            <div className="App">
                {/* Your app components */}
            </div>
        </DataDogProvider>
    );
}

// Custom hook for tracking user interactions
export function useDataDogTracking() {
    const trackUserAction = (actionName, data = {}) => {
        datadogRum.addAction(actionName, {
            ...data,
            timestamp: Date.now()
        });
    };
    
    const trackCustomError = (error, context = {}) => {
        datadogRum.addError(error, {
            ...context,
            timestamp: Date.now()
        });
    };
    
    const trackPerformanceMetric = (metricName, value, unit = 'ms') => {
        datadogRum.addAction('performance_metric', {
            metric_name: metricName,
            metric_value: value,
            metric_unit: unit,
            timestamp: Date.now()
        });
    };
    
    return {
        trackUserAction,
        trackCustomError,
        trackPerformanceMetric
    };
}

// Usage in components
function CheckoutButton({ onCheckout }) {
    const { trackUserAction, trackCustomError, trackPerformanceMetric } = useDataDogTracking();
    
    const handleCheckout = async () => {
        const startTime = performance.now();
        
        try {
            trackUserAction('checkout_started', {
                button_type: 'primary',
                cart_value: getCurrentCartValue()
            });
            
            await onCheckout();
            
            const duration = performance.now() - startTime;
            trackPerformanceMetric('checkout_duration', duration);
            
            trackUserAction('checkout_completed', {
                success: true,
                duration: duration
            });
            
        } catch (error) {
            trackCustomError(error, {
                action: 'checkout',
                cart_value: getCurrentCartValue()
            });
            
            trackUserAction('checkout_failed', {
                error_message: error.message
            });
            
            throw error;
        }
    };
    
    return (
        <button onClick={handleCheckout}>
            Checkout
        </button>
    );
}
```

### Custom Event Tracking for JSON Endpoints

#### API Monitoring Setup

```javascript
// Enhanced API monitoring with DataDog RUM
class ApiMonitor {
    constructor() {
        this.setupInterceptors();
        this.metrics = new Map();
        this.errorCounts = new Map();
    }
    
    setupInterceptors() {
        // Fetch interceptor
        const originalFetch = window.fetch;
        window.fetch = async (...args) => {
            const url = args[0];
            const options = args[1] || {};
            const startTime = performance.now();
            
            try {
                const response = await originalFetch.apply(this, args);
                const duration = performance.now() - startTime;
                
                this.trackApiCall(url, options.method || 'GET', duration, response);
                return response;
                
            } catch (error) {
                const duration = performance.now() - startTime;
                this.trackApiError(url, options.method || 'GET', duration, error);
                throw error;
            }
        };
        
        // XMLHttpRequest interceptor
        const originalXHR = window.XMLHttpRequest;
        window.XMLHttpRequest = function() {
            const xhr = new originalXHR();
            const startTime = performance.now();
            
            // Track request details
            let method, url;
            xhr.open = function(_method, _url, ...args) {
                method = _method;
                url = _url;
                return originalXHR.prototype.open.apply(xhr, [method, url, ...args]);
            };
            
            xhr.addEventListener('loadend', () => {
                const duration = performance.now() - startTime;
                const success = xhr.status >= 200 && xhr.status < 300;
                
                this.trackApiCall(url, method, duration, {
                    ok: success,
                    status: xhr.status
                });
            });
            
            xhr.addEventListener('error', () => {
                const duration = performance.now() - startTime;
                this.trackApiError(url, method, duration, new Error('Network error'));
            });
            
            return xhr;
        }.bind(this);
    }
    
    trackApiCall(url, method, duration, response) {
        // Extract endpoint name
        const endpoint = this.extractEndpoint(url);
        
        // Track in DataDog
        datadogRum.addAction('api_call', {
            endpoint: endpoint,
            method: method,
            duration: duration,
            status: response.status || (response.ok ? 200 : 500),
            success: response.ok,
            size: response.headers?.get('content-length') || 0,
            timestamp: Date.now()
        });
        
        // Track metrics for alerting
        this.updateEndpointMetrics(endpoint, duration, response.ok);
        
        // Check for slow API calls
        if (duration > 2000) {
            datadogRum.addError(new Error(`Slow API call: ${endpoint}`), {
                endpoint: endpoint,
                method: method,
                duration: duration,
                threshold: 2000,
                severity: 'warning'
            });
        }
    }
    
    trackApiError(url, method, duration, error) {
        const endpoint = this.extractEndpoint(url);
        
        datadogRum.addError(error, {
            endpoint: endpoint,
            method: method,
            duration: duration,
            error_type: this.categorizeApiError(error),
            timestamp: Date.now()
        });
        
        // Track error counts for alerting
        const errorKey = `${endpoint}:${method}`;
        const count = (this.errorCounts.get(errorKey) || 0) + 1;
        this.errorCounts.set(errorKey, count);
        
        // Alert on high error rates
        if (count >= 10) {
            datadogRum.addError(new Error(`High error rate for ${endpoint}`), {
                endpoint: endpoint,
                error_count: count,
                time_window: '5_minutes',
                severity: 'critical'
            });
        }
    }
    
    extractEndpoint(url) {
        try {
            const urlObj = new URL(url);
            return urlObj.pathname;
        } catch {
            return url;
        }
    }
    
    categorizeApiError(error) {
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
            return 'network_error';
        } else if (error.message.includes('4')) {
            return 'client_error';
        } else if (error.message.includes('5')) {
            return 'server_error';
        } else {
            return 'unknown_error';
        }
    }
    
    updateEndpointMetrics(endpoint, duration, success) {
        if (!this.metrics.has(endpoint)) {
            this.metrics.set(endpoint, {
                totalCalls: 0,
                successfulCalls: 0,
                totalDuration: 0,
                errorRate: 0,
                averageDuration: 0
            });
        }
        
        const metrics = this.metrics.get(endpoint);
        metrics.totalCalls++;
        if (success) {
            metrics.successfulCalls++;
        }
        metrics.totalDuration += duration;
        metrics.averageDuration = metrics.totalDuration / metrics.totalCalls;
        metrics.errorRate = (metrics.totalCalls - metrics.successfulCalls) / metrics.totalCalls;
    }
    
    getEndpointMetrics() {
        const summary = {
            endpoints: [],
            totalCalls: 0,
            totalErrors: 0,
            averageResponseTime: 0
        };
        
        let totalDuration = 0;
        
        this.metrics.forEach((metrics, endpoint) => {
            summary.endpoints.push({
                endpoint: endpoint,
                ...metrics
            });
            
            summary.totalCalls += metrics.totalCalls;
            summary.totalErrors += (metrics.totalCalls - metrics.successfulCalls);
            totalDuration += metrics.totalDuration;
        });
        
        summary.averageResponseTime = summary.totalCalls > 0 
            ? totalDuration / summary.totalCalls 
            : 0;
        
        return summary;
    }
}

// Initialize API monitoring
const apiMonitor = new ApiMonitor();

// Track API metrics periodically
setInterval(() => {
    const metrics = apiMonitor.getEndpointMetrics();
    datadogRum.addAction('api_metrics_summary', metrics);
}, 60000); // Every minute
```

### Performance Monitoring Setup

#### Comprehensive Performance Monitoring

```javascript
// Comprehensive performance monitoring setup
class PerformanceMonitor {
    constructor() {
        this.setupCoreWebVitals();
        this.setupCustomMetrics();
        this.setupResourceMonitoring();
        this.setupNavigationTiming();
    }
    
    setupCoreWebVitals() {
        // LCP monitoring
        const lcpObserver = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            const lastEntry = entries[entries.length - 1];
            
            datadogRum.addAction('core_web_vital_lcp', {
                value: lastEntry.startTime,
                element: lastEntry.element?.tagName || 'unknown',
                url: lastEntry.url,
                timestamp: Date.now()
            });
            
            // Alert on poor LCP
            if (lastEntry.startTime > 2500) {
                datadogRum.addError(new Error('Poor LCP detected'), {
                    lcp_value: lastEntry.startTime,
                    threshold: 2500,
                    severity: 'warning'
                });
            }
        });
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
        
        // FID monitoring
        const fidObserver = new PerformanceObserver((list) => {
            list.getEntries().forEach((entry) => {
                const fidValue = entry.processingStart - entry.startTime;
                
                datadogRum.addAction('core_web_vital_fid', {
                    value: fidValue,
                    target: entry.target?.tagName || 'unknown',
                    timestamp: Date.now()
                });
                
                // Alert on poor FID
                if (fidValue > 100) {
                    datadogRum.addError(new Error('Poor FID detected'), {
                        fid_value: fidValue,
                        threshold: 100,
                        severity: 'warning'
                    });
                }
            });
        });
        fidObserver.observe({ entryTypes: ['first-input'] });
        
        // CLS monitoring
        let clsValue = 0;
        const clsObserver = new PerformanceObserver((list) => {
            list.getEntries().forEach((entry) => {
                if (!entry.hadRecentInput) {
                    const sessionValue = entry.value;
                    const value = sessionValue - clsValue;
                    clsValue = sessionValue;
                    
                    datadogRum.addAction('core_web_vital_cls', {
                        value: value,
                        cumulative_value: clsValue,
                        sources: entry.sources?.length || 0,
                        timestamp: Date.now()
                    });
                    
                    // Alert on poor CLS
                    if (clsValue > 0.1) {
                        datadogRum.addError(new Error('Poor CLS detected'), {
                            cls_value: clsValue,
                            threshold: 0.1,
                            severity: 'warning'
                        });
                    }
                }
            });
        });
        clsObserver.observe({ entryTypes: ['layout-shift'] });
    }
    
    setupCustomMetrics() {
        // Custom performance metrics
        this.measureTimeToInteractive();
        this.measureFirstPaint();
        this.measureDOMContentLoad();
    }
    
    measureTimeToInteractive() {
        // Approximate TTI measurement
        const observer = new PerformanceObserver((list) => {
            list.getEntries().forEach((entry) => {
                if (entry.entryType === 'first-input') {
                    datadogRum.addAction('custom_metric_tti', {
                        value: entry.startTime,
                        timestamp: Date.now()
                    });
                    observer.disconnect();
                }
            });
        });
        observer.observe({ entryTypes: ['first-input'] });
    }
    
    measureFirstPaint() {
        const fpObserver = new PerformanceObserver((list) => {
            list.getEntries().forEach((entry) => {
                datadogRum.addAction('custom_metric_fp', {
                    value: entry.startTime,
                    timestamp: Date.now()
                });
            });
        });
        fpObserver.observe({ entryTypes: ['paint'] });
    }
    
    measureDOMContentLoad() {
        const navigation = performance.getEntriesByType('navigation')[0];
        if (navigation) {
            datadogRum.addAction('custom_metric_dom_content_loaded', {
                value: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
                timestamp: Date.now()
            });
        }
    }
    
    setupResourceMonitoring() {
        const resourceObserver = new PerformanceObserver((list) => {
            list.getEntries().forEach((entry) => {
                if (entry.duration > 0 && entry.initiatorType) {
                    const resourceData = {
                        name: entry.name,
                        type: entry.initiatorType,
                        duration: entry.duration,
                        size: entry.transferSize || 0,
                        cached: entry.transferSize !== entry.decodedBodySize,
                        timestamp: Date.now()
                    };
                    
                    datadogRum.addAction('resource_load', resourceData);
                    
                    // Alert on slow resources
                    if (entry.duration > 1000) {
                        datadogRum.addError(new Error(`Slow resource: ${entry.name}`), {
                            resource_name: entry.name,
                            resource_type: entry.initiatorType,
                            duration: entry.duration,
                            threshold: 1000,
                            severity: 'warning'
                        });
                    }
                }
            });
        });
        
        resourceObserver.observe({ entryTypes: ['resource'] });
    }
    
    setupNavigationTiming() {
        // Monitor navigation timing phases
        const navigation = performance.getEntriesByType('navigation')[0];
        if (navigation) {
            const timingMetrics = {
                dns_lookup: navigation.domainLookupEnd - navigation.domainLookupStart,
                tcp_connect: navigation.connectEnd - navigation.connectStart,
                server_response: navigation.responseStart - navigation.requestStart,
                content_download: navigation.responseEnd - navigation.responseStart,
                dom_processing: navigation.domComplete - navigation.responseEnd,
                total_load_time: navigation.loadEventEnd - navigation.navigationStart
            };
            
            Object.entries(timingMetrics).forEach(([phase, duration]) => {
                datadogRum.addAction('navigation_timing', {
                    phase: phase,
                    duration: duration,
                    timestamp: Date.now()
                });
            });
        }
    }
    
    // Custom performance measurement utility
    startCustomTiming(name) {
        return {
            name: name,
            startTime: performance.now(),
            end: () => {
                const duration = performance.now() - this.startTime;
                datadogRum.addAction('custom_timing', {
                    name: this.name,
                    duration: duration,
                    timestamp: Date.now()
                });
                return duration;
            }
        };
    }
}

// Initialize performance monitoring
const performanceMonitor = new PerformanceMonitor();

// Example usage of custom timing
const timing1 = performanceMonitor.startCustomTiming('user_registration');
// ... registration process ...
timing1.end();

const timing2 = performanceMonitor.startCustomTiming('data_sync');
// ... data sync process ...
timing2.end();
```

### Error Tracking Configuration

#### Comprehensive Error Tracking

```javascript
// Comprehensive error tracking configuration
class ErrorTracker {
    constructor() {
        this.setupGlobalErrorHandlers();
        this.setupUnhandledPromiseRejections();
        this.setupResourceErrorTracking();
        this.setupConsoleErrorTracking();
        this.errorCounts = new Map();
        this.lastAlertTime = new Map();
    }
    
    setupGlobalErrorHandlers() {
        // JavaScript runtime errors
        window.addEventListener('error', (event) => {
            this.trackError({
                type: 'javascript',
                message: event.message,
                filename: event.filename,
                lineno: event.lineno,
                colno: event.colno,
                error: event.error,
                timestamp: Date.now(),
                userAgent: navigator.userAgent,
                url: window.location.href,
                severity: 'error'
            });
        });
    }
    
    setupUnhandledPromiseRejections() {
        // Unhandled promise rejections
        window.addEventListener('unhandledrejection', (event) => {
            this.trackError({
                type: 'promise',
                message: event.reason?.message || 'Unhandled Promise Rejection',
                reason: event.reason,
                stack: event.reason?.stack,
                timestamp: Date.now(),
                userAgent: navigator.userAgent,
                url: window.location.href,
                severity: 'error'
            });
        });
    }
    
    setupResourceErrorTracking() {
        // Resource loading errors
        window.addEventListener('error', (event) => {
            if (event.target && (
                event.target.tagName === 'SCRIPT' ||
                event.target.tagName === 'LINK' ||
                event.target.tagName === 'IMG' ||
                event.target.tagName === 'VIDEO' ||
                event.target.tagName === 'AUDIO'
            )) {
                this.trackError({
                    type: 'resource',
                    message: `Failed to load ${event.target.tagName.toLowerCase()}: ${event.target.src || event.target.href}`,
                    target: event.target.tagName.toLowerCase(),
                    src: event.target.src || event.target.href,
                    timestamp: Date.now(),
                    url: window.location.href,
                    severity: 'warning'
                });
            }
        }, true);
    }
    
    setupConsoleErrorTracking() {
        // Track console.error calls
        const originalConsoleError = console.error;
        console.error = (...args) => {
            this.trackError({
                type: 'console_error',
                message: args.join(' '),
                args: args,
                timestamp: Date.now(),
                url: window.location.href,
                severity: 'warning'
            });
            
            // Call original console.error
            originalConsoleError.apply(console, args);
        };
    }
    
    trackError(errorData) {
        // Generate error ID
        errorData.id = this.generateErrorId();
        
        // Categorize error
        errorData.category = this.categorizeError(errorData);
        
        // Calculate severity
        errorData.severity = this.calculateSeverity(errorData);
        
        // Add context
        errorData.context = {
            userAgent: navigator.userAgent,
            viewport: `${window.innerWidth}x${window.innerHeight}`,
            url: window.location.href,
            referrer: document.referrer,
            timestamp: Date.now()
        };
        
        // Add user context if available
        if (window.currentUser) {
            errorData.context.user = {
                id: window.currentUser.id,
                role: window.currentUser.role
            };
        }
        
        // Track in DataDog
        const error = new Error(`${errorData.type}: ${errorData.message}`);
        if (errorData.stack) {
            error.stack = errorData.stack;
        }
        
        datadogRum.addError(error, {
            ...errorData,
            error_category: errorData.category,
            error_severity: errorData.severity,
            error_count: this.getErrorCount(errorData.category),
            user_session: datadogRum.getInternalContext()?.sessionId
        });
        
        // Rate limiting for alerts
        this.checkAndAlert(errorData);
        
        // Log for development
        if (process.env.NODE_ENV === 'development') {
            console.error('Enhanced error tracked:', errorData);
        }
    }
    
    categorizeError(errorData) {
        if (errorData.type === 'javascript') {
            if (errorData.message.includes('NetworkError') || 
                errorData.message.includes('fetch')) {
                return 'network';
            } else if (errorData.message.includes('ReferenceError')) {
                return 'reference';
            } else if (errorData.message.includes('TypeError')) {
                return 'type';
            } else if (errorData.message.includes('SyntaxError')) {
                return 'syntax';
            } else {
                return 'runtime';
            }
        } else if (errorData.type === 'resource') {
            return errorData.target || 'unknown';
        } else if (errorData.type === 'promise') {
            return 'async';
        } else if (errorData.type === 'console_error') {
            return 'debug';
        }
        
        return 'unknown';
    }
    
    calculateSeverity(errorData) {
        const severityMap = {
            javascript: { network: 'high', reference: 'medium', type: 'medium', runtime: 'low' },
            resource: { script: 'high', css: 'medium', img: 'low' },
            promise: 'medium',
            console_error: 'low'
        };
        
        return severityMap[errorData.type]?.[errorData.category] || 'low';
    }
    
    getErrorCount(category) {
        const count = (this.errorCounts.get(category) || 0) + 1;
        this.errorCounts.set(category, count);
        return count;
    }
    
    checkAndAlert(errorData) {
        const alertKey = `${errorData.type}:${errorData.category}`;
        const now = Date.now();
        
        // Check if we should alert (rate limit to once per 5 minutes)
        const lastAlert = this.lastAlertTime.get(alertKey);
        if (!lastAlert || now - lastAlert > 300000) {
            const errorCount = this.errorCounts.get(errorData.category) || 0;
            
            // Alert on high error counts
            if (errorCount >= 10) {
                datadogRum.addError(new Error(`High error rate: ${errorData.category}`), {
                    alert_type: 'high_error_rate',
                    category: errorData.category,
                    error_count: errorCount,
                    time_window: '5_minutes',
                    severity: 'critical'
                });
                
                this.lastAlertTime.set(alertKey, now);
            }
        }
    }
    
    generateErrorId() {
        return `err_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    
    getErrorSummary() {
        const summary = {
            totalErrors: Array.from(this.errorCounts.values()).reduce((a, b) => a + b, 0),
            byCategory: {},
            byType: {},
            trends: this.analyzeErrorTrends()
        };
        
        this.errorCounts.forEach((count, key) => {
            const [type, category] = key.split(':');
            if (!summary.byCategory[category]) {
                summary.byCategory[category] = 0;
            }
            if (!summary.byType[type]) {
                summary.byType[type] = {};
            }
            
            summary.byCategory[category] += count;
            summary.byType[type][category] = count;
        });
        
        return summary;
    }
    
    analyzeErrorTrends() {
        // Analyze error patterns
        const totalErrors = Array.from(this.errorCounts.values()).reduce((a, b) => a + b, 0);
        const mostCommon = Array.from(this.errorCounts.entries())
            .sort((a, b) => b[1] - a[1])[0];
        
        return {
            totalErrors: totalErrors,
            mostCommonError: mostCommon ? {
                category: mostCommon[0],
                count: mostCommon[1]
            } : null,
            errorRate: Math.round((totalErrors / (5 * 60)) * 60), // errors per hour
            averageErrorCount: totalErrors / this.errorCounts.size
        };
    }
}

// Initialize error tracking
const errorTracker = new ErrorTracker();

// Track error summary periodically
setInterval(() => {
    const summary = errorTracker.getErrorSummary();
    datadogRum.addAction('error_summary', summary);
}, 300000); // Every 5 minutes
```

## Best Practices

### DataDog RUM Optimization

#### Performance Optimization

```javascript
// DataDog RUM optimization best practices
class DataDogOptimizer {
    constructor() {
        this.optimizationConfig = {
            // Sampling rates optimization
            sampling: {
                development: {
                    sessionSampleRate: 100,
                    sessionReplaySampleRate: 100
                },
                staging: {
                    sessionSampleRate: 50,
                    sessionReplaySampleRate: 20
                },
                production: {
                    sessionSampleRate: 10,
                    sessionReplaySampleRate: 5
                }
            },
            
            // Data collection optimization
            collection: {
                maxEventsPerSession: 1000,
                maxResourceEntries: 500,
                maxActionEntries: 200,
                flushInterval: 30000 // 30 seconds
            },
            
            // Privacy optimization
            privacy: {
                maskUserInput: true,
                maskSensitiveRoutes: true,
                excludeInternalTraffic: true
            }
        };
    }
    
    optimizeDataCollection() {
        // Configure optimal data collection
        datadogRum.init({
            // ... other config ...
            sessionSampleRate: this.getSessionSampleRate(),
            sessionReplaySampleRate: this.getSessionReplaySampleRate(),
            
            // Control data volume
            beforeSend: (event) => {
                return this.filterEvent(event);
            },
            
            // Optimize resource tracking
            trackResources: true,
            resourceSampleRate: 50, // Sample 50% of resources
            
            // Optimize action tracking
            trackUserInteractions: true,
            defaultPrivacyLevel: 'mask-user-input'
        });
    }
    
    getSessionSampleRate() {
        const environment = this.getEnvironment();
        return this.optimizationConfig.sampling[environment].sessionSampleRate;
    }
    
    getSessionReplaySampleRate() {
        const environment = this.getEnvironment();
        return this.optimizationConfig.sampling[environment].sessionReplaySampleRate;
    }
    
    filterEvent(event) {
        // Filter out unnecessary events to reduce data volume
        
        // Skip events during development that aren't useful
        if (this.isDevelopment() && this.isDevelopmentEvent(event)) {
            return false;
        }
        
        // Skip resource events for small resources
        if (event.type === 'resource' && event.resource?.size < 1000) {
            return false;
        }
        
        // Skip action events for non-meaningful interactions
        if (event.type === 'action' && this.isMeaninglessAction(event)) {
            return false;
        }
        
        // Limit error events to prevent spam
        if (event.type === 'error' && this.isDuplicateError(event)) {
            return false;
        }
        
        return true;
    }
    
    isDevelopmentEvent(event) {
        // Filter development-specific events
        const devEvents = [
            'webpack',
            'hot-reload',
            'source-map',
            'localhost'
        ];
        
        return devEvents.some(pattern => 
            event.resource?.url?.includes(pattern) ||
            event.error?.message?.includes(pattern)
        );
    }
    
    isMeaninglessAction(event) {
        // Filter out meaningless user actions
        const meaninglessActions = [
            'scroll',
            'mousemove',
            'focus',
            'blur'
        ];
        
        return meaninglessActions.includes(event.action?.type);
    }
    
    isDuplicateError(event) {
        // Simple deduplication based on error message and stack
        const errorKey = `${event.error?.message}:${event.error?.stack?.substring(0, 100)}`;
        const now = Date.now();
        
        if (!this.lastErrorTime) {
            this.lastErrorTime = new Map();
        }
        
        const lastTime = this.lastErrorTime.get(errorKey);
        if (lastTime && now - lastTime < 5000) { // 5 second deduplication window
            return true;
        }
        
        this.lastErrorTime.set(errorKey, now);
        return false;
    }
    
    getEnvironment() {
        if (typeof window !== 'undefined') {
            const hostname = window.location.hostname;
            if (hostname.includes('localhost') || hostname.includes('127.0.0.1')) {
                return 'development';
            } else if (hostname.includes('staging')) {
                return 'staging';
            }
        }
        return 'production';
    }
    
    isDevelopment() {
        return this.getEnvironment() === 'development';
    }
    
    optimizeBundleSize() {
        // Only import what you need from DataDog SDK
        const requiredImports = [
            '@datadog/browser-rum',
            '@datadog/browser-core'
        ];
        
        console.log('DataDog bundle optimization:', {
            imports: requiredImports,
            treeShaking: true,
            deadCodeElimination: true
        });
    }
    
    optimizeNetworkUsage() {
        // Configure network optimization
        datadogRum.setGlobalContext({
            network_optimization: {
                compression_enabled: true,
                batch_size: 50,
                flush_interval: 30000
            }
        });
    }
}

// Initialize optimization
const optimizer = new DataDogOptimizer();
optimizer.optimizeDataCollection();
optimizer.optimizeBundleSize();
optimizer.optimizeNetworkUsage();
```

#### Cost Management

```javascript
// Cost management strategies for DataDog RUM
class CostManager {
    constructor() {
        this.costConfig = {
            // Sampling strategy for cost control
            samplingStrategy: {
                // High-value pages get higher sampling
                highValuePages: {
                    routes: ['/checkout', '/signup', '/dashboard'],
                    sessionSampleRate: 100,
                    sessionReplaySampleRate: 20
                },
                
                // Low-value pages get lower sampling
                lowValuePages: {
                    routes: ['/about', '/contact', '/terms'],
                    sessionSampleRate: 10,
                    sessionReplaySampleRate: 1
                }
            },
            
            // Data retention strategy
            retentionStrategy: {
                sessionReplay: {
                    highValue: 30,    // 30 days for high-value sessions
                    standard: 7      // 7 days for standard sessions
                }
            }
        };
    }
    
    implementCostControl() {
        // Dynamic sampling based on page value
        const samplingRate = this.getDynamicSamplingRate();
        
        datadogRum.init({
            // ... other config ...
            sessionSampleRate: samplingRate.session,
            sessionReplaySampleRate: samplingRate.replay,
            
            // Cost control in beforeSend
            beforeSend: (event) => {
                return this.costOptimizedFilter(event);
            }
        });
    }
    
    getDynamicSamplingRate() {
        const currentPath = window.location.pathname;
        const userValue = this.getUserValue();
        
        // High-value users get higher sampling
        if (userValue === 'high') {
            return { session: 100, replay: 20 };
        }
        
        // Check if current page is high value
        const isHighValuePage = this.costConfig.samplingStrategy.highValuePages.routes
            .some(route => currentPath.includes(route));
        
        if (isHighValuePage) {
            return { session: 50, replay: 10 };
        }
        
        // Default low sampling for cost control
        return { session: 5, replay: 1 };
    }
    
    getUserValue() {
        // Determine user value based on behavior or account type
        if (window.currentUser?.plan === 'enterprise') {
            return 'high';
        }
        
        // Check for high-value behaviors
        const sessionData = datadogRum.getInternalContext();
        if (sessionData?.user?.lifetimeValue > 1000) {
            return 'high';
        }
        
        return 'standard';
    }
    
    costOptimizedFilter(event) {
        // Filter events to reduce costs
        
        // Skip resource events for non-critical resources
        if (event.type === 'resource') {
            if (!this.isCriticalResource(event.resource?.url)) {
                return Math.random() < 0.1; // Only keep 10% of non-critical resources
            }
        }
        
        // Skip action events during idle periods
        if (event.type === 'action') {
            if (this.isIdleAction(event)) {
                return Math.random() < 0.2; // Only keep 20% of idle actions
            }
        }
        
        // Always keep error events (high value)
        if (event.type === 'error') {
            return true;
        }
        
        return true;
    }
    
    isCriticalResource(url) {
        // Define critical resources that should always be tracked
        const criticalPatterns = [
            /\.css$/,
            /main\./,
            /bundle\./,
            /runtime\./,
            /vendor\./
        ];
        
        return criticalPatterns.some(pattern => pattern.test(url));
    }
    
    isIdleAction(event) {
        // Define idle actions that can be filtered
        const idleActions = ['scroll', 'mousemove'];
        return idleActions.includes(event.action?.type);
    }
    
    monitorCostMetrics() {
        // Track cost-related metrics
        setInterval(() => {
            const context = datadogRum.getInternalContext();
            
            datadogRum.addAction('cost_metrics', {
                events_sent: context?.eventCount || 0,
                session_replay_enabled: context?.sessionReplay?.isEnabled || false,
                sampling_rate: this.getDynamicSamplingRate(),
                estimated_monthly_cost: this.estimateMonthlyCost(),
                timestamp: Date.now()
            });
        }, 300000); // Every 5 minutes
    }
    
    estimateMonthlyCost() {
        // Estimate monthly cost based on current usage
        const context = datadogRum.getInternalContext();
        const eventsPerHour = context?.eventCount / (Date.now() / (1000 * 60 * 60));
        const estimatedEventsPerMonth = eventsPerHour * 24 * 30;
        
        // DataDog pricing (approximate)
        const rumEventCost = 0.000015; // $15 per million events
        const replayCost = 0.001; // $1 per session replay
        
        const estimatedCost = estimatedEventsPerMonth * rumEventCost;
        
        return {
            estimatedEventsPerMonth: Math.round(estimatedEventsPerMonth),
            estimatedCostPerMonth: Math.round(estimatedCost * 100) / 100,
            costBreakdown: {
                rumEvents: estimatedCost * 0.8,
                sessionReplay: estimatedCost * 0.2
            }
        };
    }
    
    setCostAlerts() {
        // Set up cost alerts
        const costAlertConfig = {
            monthlyBudget: 100, // $100 monthly budget
            warningThreshold: 0.8, // Alert at 80% of budget
            criticalThreshold: 0.9 // Alert at 90% of budget
        };
        
        datadogRum.setGlobalContext({
            cost_management: costAlertConfig
        });
        
        // Monitor costs and alert when approaching budget
        setInterval(() => {
            const costMetrics = this.estimateMonthlyCost();
            const budgetUsage = costMetrics.estimatedCostPerMonth / costAlertConfig.monthlyBudget;
            
            if (budgetUsage >= costAlertConfig.criticalThreshold) {
                datadogRum.addError(new Error('Monthly budget critical'), {
                    budget_usage: budgetUsage,
                    estimated_cost: costMetrics.estimatedCostPerMonth,
                    monthly_budget: costAlertConfig.monthlyBudget,
                    severity: 'critical'
                });
            } else if (budgetUsage >= costAlertConfig.warningThreshold) {
                datadogRum.addError(new Error('Monthly budget warning'), {
                    budget_usage: budgetUsage,
                    estimated_cost: costMetrics.estimatedCostPerMonth,
                    monthly_budget: costAlertConfig.monthlyBudget,
                    severity: 'warning'
                });
            }
        }, 3600000); // Check every hour
    }
}

// Initialize cost management
const costManager = new CostManager();
costManager.implementCostControl();
costManager.monitorCostMetrics();
costManager.setCostAlerts();
```

### Alert Configuration

#### Effective Alerting Strategy

```javascript
// Comprehensive alert configuration
class AlertManager {
    constructor() {
        this.alertConfig = {
            // Performance alerts
            performance: {
                coreWebVitals: {
                    lcp: {
                        name: "LCP Performance Degradation",
                        query: "avg(last_5m):avg:rum.lcp{*} by {env,service} > 2500",
                        message: "LCP is exceeding the performance threshold",
                        tags: ["team:frontend", "severity:high"],
                        priority: 1,
                        timeout: 900 // 15 minutes
                    },
                    fid: {
                        name: "FID Performance Degradation",
                        query: "avg(last_5m):avg:rum.fid{*} by {env,service} > 100",
                        message: "FID is exceeding the performance threshold",
                        tags: ["team:frontend", "severity:high"],
                        priority: 1,
                        timeout: 900
                    },
                    cls: {
                        name: "CLS Performance Degradation",
                        query: "avg(last_5m):avg:rum.cls{*} by {env,service} > 0.1",
                        message: "CLS is exceeding the performance threshold",
                        tags: ["team:frontend", "severity:medium"],
                        priority: 2,
                        timeout: 1800 // 30 minutes
                    }
                },
                
                errorRate: {
                    name: "High Error Rate",
                    query: "sum(last_5m):sum:rum.error{*} by {env,service} > 100",
                    message: "Error rate is critically high",
                    tags: ["team:frontend", "severity:critical"],
                    priority: 0,
                    timeout: 300 // 5 minutes
                },
                
                apiPerformance: {
                    name: "API Performance Degradation",
                    query: "avg(last_5m):avg:rum.resource.duration{type:fetch} by {env,service} > 2000",
                    message: "API response times are too slow",
                    tags: ["team:backend", "severity:medium"],
                    priority: 2,
                    timeout: 1800
                }
            },
            
            // Business metric alerts
            business: {
                conversion: {
                    name: "Conversion Rate Drop",
                    query: "sum(last_1h):sum:rum.action{action_type:conversion} by {env,service} < 10",
                    message: "Conversion rate has dropped significantly",
                    tags: ["team:product", "severity:high"],
                    priority: 1,
                    timeout: 3600 // 1 hour
                },
                
                userEngagement: {
                    name: "Low User Engagement",
                    query: "sum(last_30m):sum:rum.view{*} by {env,service} < 100",
                    message: "User engagement is below normal levels",
                    tags: ["team:product", "severity:medium"],
                    priority: 3,
                    timeout: 1800
                }
            }
        };
    }
    
    configureAlerts() {
        // Set up alerting rules
        Object.values(this.alertConfig.performance).forEach(alertGroup => {
            Object.values(alertGroup).forEach(alert => {
                this.createAlert(alert);
            });
        });
        
        Object.values(this.alertConfig.business).forEach(alert => {
            this.createAlert(alert);
        });
    }
    
    createAlert(alertConfig) {
        // Create individual alert
        datadogRum.addAction('alert_configured', {
            alert_name: alertConfig.name,
            alert_query: alertConfig.query,
            alert_threshold: alertConfig.threshold,
            alert_severity: alertConfig.priority,
            alert_timeout: alertConfig.timeout
        });
    }
    
    setupAlertEscalation() {
        // Set up alert escalation policies
        const escalationRules = {
            // Critical alerts escalate immediately
            critical: {
                immediate: ['oncall@company.com', 'manager@company.com'],
                sms: ['+1234567890', '+0987654321']
            },
            
            // High priority alerts escalate after 15 minutes
            high: {
                delay: 900, // 15 minutes
                email: ['oncall@company.com'],
                sms: ['+1234567890']
            },
            
            // Medium priority alerts during business hours only
            medium: {
                businessHours: true,
                email: ['team@company.com']
            }
        };
        
        datadogRum.setGlobalContext({
            alert_escalation: escalationRules
        });
    }
    
    setupAlertRouting() {
        // Route alerts to appropriate teams
        const routingRules = {
            performance: {
                core_web_vitals: ['frontend-team'],
                error_rate: ['frontend-team', 'backend-team'],
                api_performance: ['backend-team']
            },
            business: {
                conversion: ['product-team', 'growth-team'],
                user_engagement: ['product-team']
            }
        };
        
        datadogRum.setGlobalContext({
            alert_routing: routingRules
        });
    }
    
    monitorAlertEffectiveness() {
        // Monitor and optimize alert effectiveness
        setInterval(() => {
            const alertMetrics = {
                totalAlerts: this.getTotalAlerts(),
                alertResponseTime: this.getAverageResponseTime(),
                falsePositiveRate: this.getFalsePositiveRate(),
                alertFatigue: this.getAlertFatigueScore(),
                timestamp: Date.now()
            };
            
            datadogRum.addAction('alert_effectiveness', alertMetrics);
            
            // Optimize alerts based on effectiveness
            this.optimizeAlerts(alertMetrics);
        }, 86400000); // Daily analysis
    }
    
    getTotalAlerts() {
        // Calculate total alerts fired
        return 0; // Would be calculated from DataDog metrics
    }
    
    getAverageResponseTime() {
        // Calculate average alert response time
        return 300; // Would be calculated from DataDog metrics
    }
    
    getFalsePositiveRate() {
        // Calculate false positive rate
        return 0.05; // 5% false positive rate
    }
    
    getAlertFatigueScore() {
        // Calculate alert fatigue score based on frequency and response
        const alertFrequency = this.getTotalAlerts() / 24; // per hour
        const responseRate = 0.8; // 80% response rate
        
        return Math.min(1, alertFrequency / 10 * (1 - responseRate));
    }
    
    optimizeAlerts(alertMetrics) {
        // Optimize alerts based on effectiveness metrics
        
        if (alertMetrics.falsePositiveRate > 0.1) {
            // Too many false positives, adjust thresholds
            datadogRum.addError(new Error('High false positive rate detected'), {
                current_rate: alertMetrics.falsePositiveRate,
                threshold: 0.1,
                recommendation: 'Increase alert thresholds'
            });
        }
        
        if (alertMetrics.alertFatigue > 0.7) {
            // Alert fatigue detected, reduce frequency
            datadogRum.addError(new Error('Alert fatigue detected'), {
                fatigue_score: alertMetrics.alertFatigue,
                threshold: 0.7,
                recommendation: 'Reduce alert frequency or improve routing'
            });
        }
    }
    
    setupAlertTesting() {
        // Set up alert testing and validation
        const testAlerts = {
            // Test critical path alerts
            criticalPath: {
                lcp: () => this.testLCPAlert(),
                errorRate: () => this.testErrorRateAlert(),
                apiPerformance: () => this.testAPIPerformanceAlert()
            },
            
            // Test business metric alerts
            businessMetrics: {
                conversion: () => this.testConversionAlert(),
                engagement: () => this.testEngagementAlert()
            }
        };
        
        // Run alert tests weekly
        setInterval(() => {
            Object.values(testAlerts.criticalPath).forEach(test => test());
            Object.values(testAlerts.businessMetrics).forEach(test => test());
        }, 604800000); // Weekly (7 days)
    }
    
    testLCPAlert() {
        // Test LCP alert by simulating poor performance
        datadogRum.addAction('alert_test_lcp', {
            test_type: 'lcp_alert',
            simulated_lcp: 3000, // Simulate poor LCP
            threshold: 2500,
            result: 'should_trigger_alert'
        });
    }
    
    testErrorRateAlert() {
        // Test error rate alert
        datadogRum.addAction('alert_test_error_rate', {
            test_type: 'error_rate_alert',
            simulated_errors: 150,
            threshold: 100,
            result: 'should_trigger_alert'
        });
    }
    
    testAPIPerformanceAlert() {
        // Test API performance alert
        datadogRum.addAction('alert_test_api_performance', {
            test_type: 'api_performance_alert',
            simulated_response_time: 3000,
            threshold: 2000,
            result: 'should_trigger_alert'
        });
    }
    
    testConversionAlert() {
        // Test conversion alert
        datadogRum.addAction('alert_test_conversion', {
            test_type: 'conversion_alert',
            simulated_conversions: 5,
            threshold: 10,
            result: 'should_trigger_alert'
        });
    }
    
    testEngagementAlert() {
        // Test user engagement alert
        datadogRum.addAction('alert_test_engagement', {
            test_type: 'engagement_alert',
            simulated_views: 50,
            threshold: 100,
            result: 'should_trigger_alert'
        });
    }
}

// Initialize alert management
const alertManager = new AlertManager();
alertManager.configureAlerts();
alertManager.setupAlertEscalation();
alertManager.setupAlertRouting();
alertManager.monitorAlertEffectiveness();
alertManager.setupAlertTesting();
```

### Dashboard Maintenance

#### Dashboard Optimization and Maintenance

```javascript
// Dashboard maintenance and optimization
class DashboardManager {
    constructor() {
        this.dashboardConfig = {
            // Dashboard refresh intervals
            refreshIntervals: {
                realTime: 30,      // 30 seconds for critical metrics
                nearRealTime: 300, // 5 minutes for important metrics
                hourly: 3600,      // 1 hour for trend analysis
                daily: 86400       // 24 hours for long-term trends
            },
            
            // Widget organization
            widgetGroups: {
                performance: ['core_web_vitals', 'api_performance', 'resource_loading'],
                userExperience: ['page_views', 'user_interactions', 'conversion_rates'],
                errors: ['error_rates', 'error_types', 'error_trends'],
                business: ['revenue_impact', 'user_retention', 'feature_adoption']
            }
        };
    }
    
    optimizeDashboardPerformance() {
        // Optimize dashboard loading and performance
        
        // Use efficient queries
        const optimizedQueries = {
            // Use aggregation for better performance
            coreWebVitals: "avg:rum.lcp{*} by {env,service}.rollup(300)",
            errorRate: "sum:rum.error{*} by {env,service}.rollup(300)",
            pageViews: "sum:rum.view{*} by {env,service}.rollup(300)",
            
            // Use sampling for high-volume metrics
            userInteractions: "sum:rum.action{*} by {env,service}.rollup(600).sample(10)",
            resourceLoading: "avg:rum.resource.duration{*} by {env,service}.rollup(300)"
        };
        
        // Configure dashboard widgets with optimal refresh rates
        const widgets = Object.entries(this.dashboardConfig.widgetGroups).map(([group, widgets]) => ({
            group: group,
            refreshInterval: this.getOptimalRefreshInterval(group),
            widgets: widgets.map(widget => ({
                name: widget,
                query: optimizedQueries[widget],
                type: this.getWidgetType(widget)
            }))
        }));
        
        return widgets;
    }
    
    getOptimalRefreshInterval(group) {
        const intervals = {
            performance: this.dashboardConfig.refreshIntervals.realTime,
            errors: this.dashboardConfig.refreshIntervals.realTime,
            userExperience: this.dashboardConfig.refreshIntervals.nearRealTime,
            business: this.dashboardConfig.refreshIntervals.hourly
        };
        
        return intervals[group] || this.dashboardConfig.refreshIntervals.nearRealTime;
    }
    
    getWidgetType(widgetName) {
        const widgetTypes = {
            core_web_vitals: 'timeseries',
            api_performance: 'timeseries',
            resource_loading: 'timeseries',
            page_views: 'timeseries',
            user_interactions: 'query_table',
            conversion_rates: 'timeseries',
            error_rates: 'timeseries',
            error_types: 'toplist',
            error_trends: 'timeseries',
            revenue_impact: 'timeseries',
            user_retention: 'timeseries',
            feature_adoption: 'timeseries'
        };
        
        return widgetTypes[widgetName] || 'timeseries';
    }
    
    implementDashboardAlerting() {
        // Set up dashboard-specific alerts
        
        const dashboardAlerts = {
            // Alert when dashboard widgets fail to load
            widgetFailures: {
                name: "Dashboard Widget Failure",
                condition: "avg(last_5m):dashboard.widget.error{*} > 0",
                message: "One or more dashboard widgets are failing to load",
                severity: "medium"
            },
            
            // Alert on data gaps
            dataGaps: {
                name: "Data Gap Detected",
                condition: "avg(last_10m):rum.view{*} by {env,service} = 0",
                message: "No data has been received for 10 minutes",
                severity: "high"
            },
            
            // Alert on dashboard performance issues
            dashboardPerformance: {
                name: "Dashboard Performance Issue",
                condition: "avg(last_5m):dashboard.load.time{*} > 5000",
                message: "Dashboard is taking too long to load",
                severity: "low"
            }
        };
        
        return dashboardAlerts;
    }
    
    setupDashboardHealthMonitoring() {
        // Monitor dashboard health and performance
        
        const healthMetrics = {
            // Track widget loading times
            widgetLoadTimes: [],
            
            // Track query performance
            queryPerformance: [],
            
            // Track data freshness
            dataFreshness: [],
            
            // Track user interactions
            userInteractions: []
        };
        
        // Monitor widget performance
        setInterval(() => {
            const performanceMetrics = {
                timestamp: Date.now(),
                averageWidgetLoadTime: this.calculateAverageWidgetLoadTime(),
                slowestWidget: this.getSlowestWidget(),
                queryTimeouts: this.getQueryTimeouts(),
                dataFreshness: this.getDataFreshnessScore()
            };
            
            datadogRum.addAction('dashboard_health', performanceMetrics);
            
            // Alert on performance issues
            if (performanceMetrics.averageWidgetLoadTime > 2000) {
                datadogRum.addError(new Error('Dashboard performance degradation'), {
                    average_load_time: performanceMetrics.averageWidgetLoadTime,
                    threshold: 2000,
                    slowest_widget: performanceMetrics.slowestWidget,
                    severity: 'warning'
                });
            }
            
            if (performanceMetrics.dataFreshness < 0.9) {
                datadogRum.addError(new Error('Data freshness issue'), {
                    freshness_score: performanceMetrics.dataFreshness,
                    threshold: 0.9,
                    timeout_count: performanceMetrics.queryTimeouts,
                    severity: 'high'
                });
            }
        }, 300000); // Every 5 minutes
    }
    
    calculateAverageWidgetLoadTime() {
        // Calculate average widget load time
        return Math.random() * 1000 + 500; // Mock implementation
    }
    
    getSlowestWidget() {
        // Get the slowest performing widget
        return { name: 'resource_analysis', loadTime: 3000 };
    }
    
    getQueryTimeouts() {
        // Get number of query timeouts
        return Math.floor(Math.random() * 10);
    }
    
    getDataFreshnessScore() {
        // Calculate data freshness score (0-1)
        return 0.95; // Mock implementation
    }
    
    implementDashboardAutoScaling() {
        // Automatically scale dashboard resources based on usage
        
        const autoScalingRules = {
            // Scale based on concurrent users
            concurrentUsers: {
                threshold: 10,
                action: 'increase_refresh_frequency'
            },
            
            // Scale based on data volume
            dataVolume: {
                threshold: 1000000, // 1M events per hour
                action: 'enable_aggregation'
            },
            
            // Scale based on query complexity
            queryComplexity: {
                threshold: 1000, // 1 second average query time
                action: 'simplify_queries'
            }
        };
        
        // Monitor scaling triggers
        setInterval(() => {
            const scalingMetrics = {
                concurrentUsers: this.getConcurrentUsers(),
                dataVolume: this.getDataVolume(),
                queryComplexity: this.getQueryComplexity()
            };
            
            Object.entries(autoScalingRules).forEach(([metric, rule]) => {
                if (scalingMetrics[metric] > rule.threshold) {
                    this.executeScalingAction(rule.action, scalingMetrics[metric]);
                }
            });
        }, 600000); // Every 10 minutes
    }
    
    getConcurrentUsers() {
        // Get number of concurrent dashboard users
        return 5; // Mock implementation
    }
    
    getDataVolume() {
        // Get current data volume
        return 500000; // Mock implementation
    }
    
    getQueryComplexity() {
        // Get average query execution time
        return 500; // Mock implementation
    }
    
    executeScalingAction(action, currentValue) {
        // Execute scaling action
        const actions = {
            increase_refresh_frequency: () => {
                datadogRum.addAction('dashboard_scaling', {
                    action: 'increase_refresh_frequency',
                    reason: 'high_concurrent_users',
                    value: currentValue,
                    timestamp: Date.now()
                });
            },
            
            enable_aggregation: () => {
                datadogRum.addAction('dashboard_scaling', {
                    action: 'enable_aggregation',
                    reason: 'high_data_volume',
                    value: currentValue,
                    timestamp: Date.now()
                });
            },
            
            simplify_queries: () => {
                datadogRum.addAction('dashboard_scaling', {
                    action: 'simplify_queries',
                    reason: 'high_query_complexity',
                    value: currentValue,
                    timestamp: Date.now()
                });
            }
        };
        
        const executeAction = actions[action];
        if (executeAction) {
            executeAction();
        }
    }
    
    setupDashboardDocumentation() {
        // Set up dashboard documentation and onboarding
        
        const dashboardDocumentation = {
            // Dashboard purpose and usage
            purpose: "Website performance and user experience monitoring",
            
            // Widget descriptions
            widgets: {
                core_web_vitals: {
                    description: "Core Web Vitals performance metrics (LCP, FID, CLS)",
                    usage: "Monitor page loading performance and user experience",
                    thresholds: {
                        lcp: "Good: < 2.5s, Needs Improvement: 2.5-4s, Poor: > 4s",
                        fid: "Good: < 100ms, Needs Improvement: 100-300ms, Poor: > 300ms",
                        cls: "Good: < 0.1, Needs Improvement: 0.1-0.25, Poor: > 0.25"
                    }
                },
                
                error_rates: {
                    description: "JavaScript and API error rates",
                    usage: "Monitor application reliability and error trends",
                    thresholds: {
                        error_rate: "Alert when error rate exceeds 5% of total requests"
                    }
                },
                
                user_engagement: {
                    description: "User engagement and interaction metrics",
                    usage: "Track user behavior and feature adoption",
                    thresholds: {
                        page_views: "Monitor significant drops in user activity",
                        conversion_rate: "Alert when conversion rate drops below expected levels"
                    }
                }
            },
            
            // Alert procedures
            alert_procedures: {
                critical: "Immediate response required - page 24/7 oncall",
                high: "Response within 15 minutes - escalate to team lead",
                medium: "Response within 1 hour - standard business hours",
                low: "Response within 24 hours - next business day"
            }
        };
        
        return dashboardDocumentation;
    }
    
    scheduleDashboardMaintenance() {
        // Schedule regular dashboard maintenance
        
        const maintenanceSchedule = {
            // Daily maintenance
            daily: {
                time: "02:00 AM",
                tasks: [
                    "Verify data freshness",
                    "Check widget performance",
                    "Review alert effectiveness"
                ]
            },
            
            // Weekly maintenance
            weekly: {
                time: "Sunday 03:00 AM",
                tasks: [
                    "Update dashboard queries",
                    "Review and optimize widget configurations",
                    "Test alert functionality",
                    "Update documentation"
                ]
            },
            
            // Monthly maintenance
            monthly: {
                time: "1st of month 04:00 AM",
                tasks: [
                    "Performance review and optimization",
                    "Cost analysis and optimization",
                    "User feedback analysis",
                    "Plan improvements for next month"
                ]
            }
        };
        
        return maintenanceSchedule;
    }
}

// Initialize dashboard management
const dashboardManager = new DashboardManager();
dashboardManager.optimizeDashboardPerformance();
dashboardManager.implementDashboardAlerting();
dashboardManager.setupDashboardHealthMonitoring();
dashboardManager.implementDashboardAutoScaling();
dashboardManager.setupDashboardDocumentation();
dashboardManager.scheduleDashboardMaintenance();
```

## Conclusion

DataDog Real User Monitoring (RUM) provides a comprehensive solution for website monitoring that eliminates the need for custom infrastructure while delivering deep insights into user experience and application performance. By following this guide, you can implement a robust monitoring system that scales with your application and provides actionable insights.

### Key Takeaways

1. **Start with Core Web Vitals**: Focus on LCP, FID, and CLS as your primary performance indicators
2. **Configure Smart Sampling**: Use appropriate sampling rates to balance data collection with cost
3. **Set Up Meaningful Alerts**: Configure alerts that provide actionable insights without alert fatigue
4. **Monitor Business Metrics**: Track conversion rates and user engagement alongside technical metrics
5. **Optimize Continuously**: Regularly review and optimize your monitoring setup based on usage patterns

### Next Steps

1. **Implement Gradually**: Start with basic DataDog RUM setup and expand features over time
2. **Customize for Your Needs**: Adapt the configurations and dashboards to your specific requirements
3. **Train Your Team**: Ensure your team understands how to use and interpret the monitoring data
4. **Establish Processes**: Create runbooks and procedures for responding to alerts and issues
5. **Measure ROI**: Track the impact of monitoring on development velocity and user experience

By leveraging DataDog RUM effectively, you'll gain comprehensive visibility into your website's performance and user experience, enabling you to proactively identify and resolve issues before they impact your users.

---

*This guide provides comprehensive coverage of DataDog RUM implementation for website monitoring. Remember to adapt the configurations and examples to your specific application requirements and DataDog subscription plan.*
