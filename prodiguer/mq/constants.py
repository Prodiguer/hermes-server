# -*- coding: utf-8 -*-

"""
.. module:: prodiguer.mq.constants.py
   :platform: Unix
   :synopsis: Prodiguer mq constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# AMPQ message exchange types.
AMPQ_EXCHANGE_TYPE_DIRECT = "direct"
AMPQ_EXCHANGE_TYPE_FANOUT = "fanout"
AMPQ_EXCHANGE_TYPE_HEADER = "header"
AMPQ_EXCHANGE_TYPE_TOPIC = "topic"

# All AMPQ exchange types.
AMPQ_EXCHANGE_TYPES = set([
	AMPQ_EXCHANGE_TYPE_DIRECT,
	AMPQ_EXCHANGE_TYPE_FANOUT,
	AMPQ_EXCHANGE_TYPE_HEADER,
	AMPQ_EXCHANGE_TYPE_TOPIC
	])

# AMPQ message delivery modes.
AMPQ_DELIVERY_MODE_NON_PERSISTENT = 1
AMPQ_DELIVERY_MODE_PERSISTENT = 2

# All AMPQ message delivery modes.
AMPQ_DELIVERY_MODES = set([
	AMPQ_DELIVERY_MODE_NON_PERSISTENT,
	AMPQ_DELIVERY_MODE_PERSISTENT
	])

# Message server virtual host.
VHOST = "prodiguer"

# Message server exchanges.
EXCHANGE_PRODIGUER_PRIMARY = "x-primary"
EXCHANGE_PRODIGUER_SECONDARY = "x-secondary"
EXCHANGE_PRODIGUER_SECONDARY_DELAYED = "x-secondary-delayed"

# All exchanges.
EXCHANGES = set([
	EXCHANGE_PRODIGUER_PRIMARY,
	EXCHANGE_PRODIGUER_SECONDARY,
	EXCHANGE_PRODIGUER_SECONDARY_DELAYED
	])

# Live message queues.
QUEUE_LIVE_CV = 'live-cv'
QUEUE_LIVE_FE = 'live-fe'
QUEUE_LIVE_METRICS_ENV = 'live-metrics-env'
QUEUE_LIVE_METRICS_PCMDI = 'live-metrics-pcmdi'
QUEUE_LIVE_MONITORING_COMPUTE = "live-monitoring-compute"
QUEUE_LIVE_MONITORING_POST_PROCESSING = "live-monitoring-post-processing"
QUEUE_LIVE_SMTP = 'live-smtp'
QUEUE_LIVE_SUPERVISEUR = 'live-superviseur'

# Debug message queues.
QUEUE_DEBUG_0000 = 'debug-0000'
QUEUE_DEBUG_0100 = 'debug-0100'
QUEUE_DEBUG_1000 = 'debug-1000'
QUEUE_DEBUG_1100 = 'debug-1100'
QUEUE_DEBUG_1199 = 'debug-1199'
QUEUE_DEBUG_2000 = 'debug-2000'
QUEUE_DEBUG_2100 = 'debug-2100'
QUEUE_DEBUG_2199 = 'debug-2199'
QUEUE_DEBUG_2900 = 'debug-2900'
QUEUE_DEBUG_3000 = 'debug-3000'
QUEUE_DEBUG_3100 = 'debug-3100'
QUEUE_DEBUG_3199 = 'debug-3199'
QUEUE_DEBUG_3900 = 'debug-3900'
QUEUE_DEBUG_7000 = 'debug-7000'
QUEUE_DEBUG_7100 = 'debug-7100'
QUEUE_DEBUG_8000 = 'debug-8000'
QUEUE_DEBUG_8100 = 'debug-8100'
QUEUE_DEBUG_8200 = 'debug-8200'
QUEUE_DEBUG_9999 = 'debug-9999'
QUEUE_DEBUG_CV = 'debug-cv'
QUEUE_DEBUG_FE = 'debug-fe'
QUEUE_DEBUG_SMTP = 'debug-smtp'

# All queues.
QUEUES = set([
	# Live queues.
	QUEUE_LIVE_CV,
	QUEUE_LIVE_FE,
	QUEUE_LIVE_METRICS_ENV,
	QUEUE_LIVE_METRICS_PCMDI,
	QUEUE_LIVE_MONITORING_COMPUTE,
	QUEUE_LIVE_MONITORING_POST_PROCESSING,
	QUEUE_LIVE_SMTP,
	QUEUE_LIVE_SUPERVISEUR,
	# Debug queues.
	QUEUE_DEBUG_0000,
	QUEUE_DEBUG_0100,
	QUEUE_DEBUG_1000,
	QUEUE_DEBUG_1100,
	QUEUE_DEBUG_1199,
	QUEUE_DEBUG_2000,
	QUEUE_DEBUG_2100,
	QUEUE_DEBUG_2199,
	QUEUE_DEBUG_2900,
	QUEUE_DEBUG_3000,
	QUEUE_DEBUG_3100,
	QUEUE_DEBUG_3199,
	QUEUE_DEBUG_3900,
	QUEUE_DEBUG_7000,
	QUEUE_DEBUG_7100,
	QUEUE_DEBUG_8000,
	QUEUE_DEBUG_8100,
	QUEUE_DEBUG_8200,
	QUEUE_DEBUG_9999,
	QUEUE_DEBUG_CV,
	QUEUE_DEBUG_FE,
	QUEUE_DEBUG_SMTP
	])

# Message producers.
PRODUCER_IGCM = "libigcm"
PRODUCER_PRODIGUER = "prodiguer"

# All producers.
PRODUCERS = set([
	PRODUCER_IGCM,
	PRODUCER_PRODIGUER
	])

# Message server users.
USER_PRODIGUER = "prodiguer-mq-user"
USER_PRODIGUER_ADMIN = "prodiguer-mq-admin"

# All users.
USERS = set([
	USER_PRODIGUER,
	USER_PRODIGUER_ADMIN
	])

# Message application identifiers.
APP_INTERNAL = "internal"
APP_MONITORING = "monitoring"
APP_METRICS = "metrics"
APP_SUPERVISEUR = "superviseur"

# All apps.
APPS = set([
	APP_INTERNAL,
	APP_METRICS,
	APP_MONITORING,
	APP_SUPERVISEUR
	])

# Message types:
# ... general message types.
MESSAGE_TYPE_0000 = "0000"		# Monitoring - simulation initialiation
MESSAGE_TYPE_0100 = "0100"		# Monitoring - simulation ends
MESSAGE_TYPE_1000 = "1000"		# Monitoring - job begins
MESSAGE_TYPE_1100 = "1100"		# Monitoring - job ends
MESSAGE_TYPE_1199 = "1199"		# Monitoring - job warning delay
MESSAGE_TYPE_2000 = "2000"		# Monitoring - post-processing job begins
MESSAGE_TYPE_2100 = "2100"		# Monitoring - post-processing job ends
MESSAGE_TYPE_2199 = "2199"		# Monitoring - post-processing job warning delay
MESSAGE_TYPE_2900 = "2900"		# Monitoring - post-processing job fails
MESSAGE_TYPE_3000 = "3000"		# Monitoring - post-processing job from checker begins
MESSAGE_TYPE_3100 = "3100"		# Monitoring - post-processing job from checker ends
MESSAGE_TYPE_3199 = "3199"		# Monitoring - post-processing job from checker warning delay
MESSAGE_TYPE_3900 = "3900"		# Monitoring - post-processing job from checker fails
MESSAGE_TYPE_7000 = "7000"		# Metrics - environment
MESSAGE_TYPE_7100 = "7100"		# Metrics - pcmdi
MESSAGE_TYPE_8000 = "8000"		# Supervisor - detect
MESSAGE_TYPE_8100 = "8100"		# Supervisor - format
MESSAGE_TYPE_8200 = "8200"		# Supervisor - dispatch
MESSAGE_TYPE_9999 = "9999"		# Monitoring - simulation stopped due to error
MESSAGE_TYPE_CV = "-1000"		# Internal - controlled vocabulary
MESSAGE_TYPE_FE = "-2000"		# Internal - front end notifications
MESSAGE_TYPE_SMTP = "-3000"		# Internal - smtp inputs


# All types.
TYPES = set([
	# ... monitoring - simulation
	MESSAGE_TYPE_0000,
	MESSAGE_TYPE_0100,
	MESSAGE_TYPE_9999,
	# ... monitoring - compute jobs
	MESSAGE_TYPE_1000,
	MESSAGE_TYPE_1100,
	MESSAGE_TYPE_1199,
	# ... monitoring - post-processing jobs
	MESSAGE_TYPE_2000,
	MESSAGE_TYPE_2100,
	MESSAGE_TYPE_2199,
	MESSAGE_TYPE_2900,
	# ... monitoring - post-processing from checker jobs
	MESSAGE_TYPE_3000,
	MESSAGE_TYPE_3100,
	MESSAGE_TYPE_3199,
	MESSAGE_TYPE_3900,
	# ... metrics
	MESSAGE_TYPE_7000,
	MESSAGE_TYPE_7100,
	# ... supervisor
	MESSAGE_TYPE_8000,
	MESSAGE_TYPE_8100,
	MESSAGE_TYPE_8200,
	# ... internal
	MESSAGE_TYPE_FE,
	MESSAGE_TYPE_CV,
	MESSAGE_TYPE_SMTP
	])

# Map of applications to message types.
MESSAGE_TYPE_APPLICATION = {
	# ... monitoring - simulation
	MESSAGE_TYPE_0000: APP_MONITORING,
	MESSAGE_TYPE_0100: APP_MONITORING,
	MESSAGE_TYPE_9999: APP_MONITORING,
	# ... monitoring - compute jobs
	MESSAGE_TYPE_1000: APP_MONITORING,
	MESSAGE_TYPE_1100: APP_MONITORING,
	MESSAGE_TYPE_1199: APP_MONITORING,
	# ... monitoring - post-processing jobs
	MESSAGE_TYPE_2000: APP_MONITORING,
	MESSAGE_TYPE_2100: APP_MONITORING,
	MESSAGE_TYPE_2199: APP_MONITORING,
	MESSAGE_TYPE_2900: APP_MONITORING,
	# ... monitoring - post-processing from checker jobs
	MESSAGE_TYPE_3000: APP_MONITORING,
	MESSAGE_TYPE_3100: APP_MONITORING,
	MESSAGE_TYPE_3199: APP_MONITORING,
	MESSAGE_TYPE_3900: APP_MONITORING,
	# ... metrics
	MESSAGE_TYPE_7000: APP_METRICS,
	MESSAGE_TYPE_7100: APP_METRICS,
	# ... supervisor
	MESSAGE_TYPE_8000: APP_SUPERVISEUR,
	MESSAGE_TYPE_8100: APP_SUPERVISEUR,
	MESSAGE_TYPE_8200: APP_SUPERVISEUR,
	# ... other
	MESSAGE_TYPE_FE: APP_INTERNAL,
	MESSAGE_TYPE_CV: APP_INTERNAL,
	MESSAGE_TYPE_SMTP: APP_INTERNAL
}

# Map of exchanges to message types.
MESSAGE_TYPE_EXCHANGE = {
	# ... monitoring - simulation
	MESSAGE_TYPE_0000: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_0100: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_9999: EXCHANGE_PRODIGUER_PRIMARY,
	# ... monitoring - compute jobs
	MESSAGE_TYPE_1000: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_1100: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_1199: EXCHANGE_PRODIGUER_SECONDARY_DELAYED,
	# ... monitoring - post-processing jobs
	MESSAGE_TYPE_2000: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_2100: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_2199: EXCHANGE_PRODIGUER_SECONDARY_DELAYED,
	MESSAGE_TYPE_2900: EXCHANGE_PRODIGUER_PRIMARY,
	# ... monitoring - post-processing from checker jobs
	MESSAGE_TYPE_3000: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_3100: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_3199: EXCHANGE_PRODIGUER_SECONDARY_DELAYED,
	MESSAGE_TYPE_3900: EXCHANGE_PRODIGUER_PRIMARY,
	# ... metrics
	MESSAGE_TYPE_7000: EXCHANGE_PRODIGUER_PRIMARY,
	MESSAGE_TYPE_7100: EXCHANGE_PRODIGUER_PRIMARY,
	# ... supervisor
	MESSAGE_TYPE_8000: EXCHANGE_PRODIGUER_SECONDARY,
	MESSAGE_TYPE_8100: EXCHANGE_PRODIGUER_SECONDARY,
	MESSAGE_TYPE_8200: EXCHANGE_PRODIGUER_SECONDARY,
	# ... other
	MESSAGE_TYPE_FE: EXCHANGE_PRODIGUER_SECONDARY,
	MESSAGE_TYPE_CV: EXCHANGE_PRODIGUER_SECONDARY,
	MESSAGE_TYPE_SMTP: EXCHANGE_PRODIGUER_SECONDARY
}

# Timestamp precision types.
TIMESTAMP_PRECISION_NS = 'ns'
TIMESTAMP_PRECISION_MS = 'ms'

# All timestamp precision types.
TIMESTAMP_PRECISIONS = set([
	TIMESTAMP_PRECISION_NS,
	TIMESTAMP_PRECISION_MS
	])

# Content types.
CONTENT_TYPE_JSON = 'application/json'
CONTENT_TYPE_BASE64 = 'application/base64'
CONTENT_TYPE_BASE64_JSON = 'application/base64+json'

# All content types.
CONTENT_TYPES = set([
	CONTENT_TYPE_JSON,
	CONTENT_TYPE_BASE64,
	CONTENT_TYPE_BASE64_JSON,
	])

# Content encodings.
CONTENT_ENCODING_UNICODE = "utf-8"

# All content encodings.
CONTENT_ENCODINGS = set([
	CONTENT_ENCODING_UNICODE
	])

# Message priorities.
PRIORITY_LOW = 1
PRIORITY_NORMAL = 4
PRIORITY_HIGH = 7
PRIORITY_URGENT = 9
PRIORITY_CRITICAL = 10

# All message priorities.
PRIORITIES = set([
	PRIORITY_LOW,
	PRIORITY_NORMAL,
	PRIORITY_HIGH,
	PRIORITY_URGENT,
	PRIORITY_CRITICAL,
	])

