import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/NotFound";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import Home from "./pages/Home";
import WorkerConsole from "./pages/WorkerConsole";
import BookingTrack from "./pages/BookingTrack";
import WorkerSignup from "./pages/WorkerSignup";
import AdminVerification from "./pages/AdminVerification";
import WorkerDashboard from "./pages/WorkerDashboard";
import WorkerApplicationStatus from "./pages/WorkerApplicationStatus";
import AdminBookings from "./pages/AdminBookings";

function Router() {
  return <Switch>
    <Route path="/" component={Home} />
    <Route path="/console" component={WorkerConsole} />
    <Route path="/track" component={BookingTrack} />
    <Route path="/become-a-worker" component={WorkerSignup} />
    <Route path="/admin/verification" component={AdminVerification} />
    <Route path="/admin/bookings" component={AdminBookings} />
    <Route path="/worker/dashboard" component={WorkerDashboard} />
    <Route path="/worker/application-status" component={WorkerApplicationStatus} />
    <Route path="/worker/onboarding" component={WorkerDashboard} />
    <Route path="/404" component={NotFound} />
    <Route component={NotFound} />
  </Switch>;
}

function App() {
  return <ErrorBoundary>
    <ThemeProvider defaultTheme="light">
      <TooltipProvider>
        <Toaster />
        <Router />
      </TooltipProvider>
    </ThemeProvider>
  </ErrorBoundary>;
}

export default App;
