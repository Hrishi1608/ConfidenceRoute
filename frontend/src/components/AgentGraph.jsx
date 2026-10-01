export default function AgentGraph({ steps, isRunning }) {
  if (steps.length === 0 && !isRunning) return null;

  return (
    <div className={`card ${isRunning ? 'animate-pulse-border' : ''}`}>
      <h3 style={{ marginTop: 0, marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
        </svg>
        Live Execution Graph
      </h3>
      
      <div className="graph-container">
        {steps.map((step, index) => {
          let badgeClass = "badge";
          if (step.confidence !== undefined) {
            if (step.confidence > 0.4) badgeClass += " high-confidence";
            else badgeClass += " low-confidence";
          }

          return (
            <div key={index} className="step-item animate-slide-up" style={{ animationDelay: `${index * 0.1}s` }}>
              <div className="step-content">
                <div className="step-header">
                  <span className="step-title">{step.step.replace(/_/g, ' ')}</span>
                  <span className="badge" style={{ background: 'var(--accent-hover)', color: 'white', border: 'none' }}>
                    {step.model}
                  </span>
                </div>
                
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.9rem', color: 'var(--text)' }}>
                  <span>Confidence Score:</span>
                  <span className={badgeClass}>
                    {step.confidence !== undefined ? step.confidence.toFixed(2) : "N/A"}
                  </span>
                </div>

                {step.verification && (
                  <div style={{ marginTop: '12px', padding: '12px', background: 'var(--bg-card)', borderRadius: '6px', fontSize: '0.85rem', borderLeft: '3px solid var(--accent)' }}>
                    <strong>Verification:</strong> {step.verification}
                  </div>
                )}
              </div>
            </div>
          );
        })}

        {isRunning && (
          <div className="step-item animate-slide-up" style={{ opacity: 0.6 }}>
            <div className="step-content" style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '24px' }}>
              <div className="spinner animate-spin" style={{ borderColor: 'rgba(0,0,0,0.1)', borderTopColor: 'var(--accent)' }}></div>
              <span>Agent is thinking...</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
