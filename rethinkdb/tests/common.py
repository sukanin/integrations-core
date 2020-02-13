# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.utils.common import get_docker_hostname

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

CHECK_NAME = 'rethinkdb'

IMAGE = 'rethinkdb:2.4.0'
CONTAINER_NAME = 'rethinkdb'
SERVER_NAME = 'server0'

HOST = get_docker_hostname()
PORT = 28015

SYSTEM_STATISTICS_METRICS = (
    'rethinkdb.stats.cluster.queries_per_sec',
    'rethinkdb.stats.cluster.read_docs_per_sec',
    'rethinkdb.stats.cluster.written_docs_per_sec',
    'rethinkdb.stats.server.queries_per_sec',
    'rethinkdb.stats.server.queries_total',
    'rethinkdb.stats.server.read_docs_per_sec',
    'rethinkdb.stats.server.read_docs_total',
    'rethinkdb.stats.server.written_docs_per_sec',
    'rethinkdb.stats.server.written_docs_total',
    'rethinkdb.stats.server.client_connections',
    'rethinkdb.stats.server.clients_active',  # NOTE: sent, but not documented on the RethinkDB website.
    # WIP
    # TODO: add a database, tables and replicas to the Docker Compose setup.
    # 'rethinkdb.stats.table.read_docs_per_sec',
    # 'rethinkdb.stats.table.written_docs_per_sec',
    # 'rethinkdb.stats.table_server.read_docs_per_sec',
    # 'rethinkdb.stats.table_server.read_docs_total',
    # 'rethinkdb.stats.table_server.written_docs_per_sec',
    # 'rethinkdb.stats.table_server.written_docs_total',
    # 'rethinkdb.stats.table_server.cache.in_use_bytes',
    # 'rethinkdb.stats.table_server.disk.read_bytes_per_sec',
    # 'rethinkdb.stats.table_server.disk.read_bytes_total',
    # 'rethinkdb.stats.table_server.disk.written_bytes_per_sec',
    # 'rethinkdb.stats.table_server.disk.written_bytes_total',
    # 'rethinkdb.stats.table_server.disk.space_usage.metadata_bytes',
    # 'rethinkdb.stats.table_server.disk.space_usage.data_bytes',
    # 'rethinkdb.stats.table_server.disk.space_usage.garbage_bytes',
    # 'rethinkdb.stats.table_server.disk.space_usage.preallocated_bytes',
)

STATUS_METRICS = (
    'rethinkdb.table_status.ready_for_outdated_reads' 'rethinkdb.table_status.ready_for_reads',
    'rethinkdb.table_status.ready_for_writes',
    'rethinkdb.table_status.all_replicas_ready',
    'rethinkdb.table_status.shards.total',
    'rethinkdb.table_status.shards.replicas.total',
    'rethinkdb.table_status.shards.replicas.state',
    'rethinkdb.server_status.network.time_connected',
    'rethinkdb.server_status.network.connected_to',
    'rethinkdb.server_status.process.time_started',
)

SYSTEM_JOBS_METRICS = (
    'rethinkdb.jobs.query.duration',
    'rethinkdb.jobs.index_construction.duration',
    'rethinkdb.jobs.index_construction.progress',
    'rethinkdb.jobs.backfill.duration',
    'rethinkdb.jobs.backfill.progress',
)

SYSTEM_CURRENT_ISSUES_METRICS = (
    'rethinkdb.current_issues.log_write_error.total',
    'rethinkdb.current_issues.server_name_collision.total',
    'rethinkdb.current_issues.db_name_collision.total',
    'rethinkdb.current_issues.table_name_collision.total',
    'rethinkdb.current_issues.outdated_index.total',
    'rethinkdb.current_issues.table_availability.total',
    'rethinkdb.current_issues.memory_error.total',
    'rethinkdb.current_issues.non_transitive_error.total',
)

# WIP
METRICS = SYSTEM_STATISTICS_METRICS